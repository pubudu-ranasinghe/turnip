import sys
import traceback
from PyQt5.QtCore import QObject, QThreadPool, QRunnable
from PyQt5.QtCore import pyqtSignal, pyqtSlot, pyqtProperty, QUrl
from beets.ui import UserError  # TODO Change to own error type
from beets import config, logging
from importer import TurnipImporter, Item
from importadapter import (ImportAdapter, ImportEvent,
                           UserAction, ActionType, EventType)


logger = logging.getLogger("turnip")
logger.setLevel(logging.DEBUG)


class ImportHandler(QObject):
    """
    Responsible for updating the UI and responding to user input
    and communicating back and forth with `TurnipImportSession`.
    """

    _current_item: Item
    _loading_status = False

    def __init__(self, beets, adapter: ImportAdapter):
        QObject.__init__(self)
        self._threadpool = QThreadPool()
        self._lib = beets.lib
        self.adapter = adapter
        self.adapter.on_event(self.handle_event)
        logger.debug(f"Maximum of {self._threadpool.maxThreadCount()} threads")
        self._current_item = Item("path")

    def handle_event(self, e: ImportEvent):
        logger.debug(f"Received event {e.event_type}")
        if e.event_type is EventType.ASK_ALBUM:
            self.set_current_item(e.payload)
        else:
            pass

    currentItemChanged = pyqtSignal("QVariantMap")

    def get_current_item(self):
        return self._current_item.to_dict()

    def set_current_item(self, item: Item):
        self._current_item = item
        self.currentItemChanged.emit(item.to_dict())

    currentItem = pyqtProperty(
        "QVariantMap",
        get_current_item,
        set_current_item,
        notify=currentItemChanged
    )

    loadingStatusChanged = pyqtSignal(bool)

    def get_loading_status(self):
        return self._loading_status

    def set_loading_status(self, status: bool):
        self._loading_status = status
        self.loadingStatusChanged.emit(status)

    loadingStatus = pyqtProperty(
        bool,
        get_loading_status,
        set_loading_status,
        notify=loadingStatusChanged
    )

    endSession = pyqtSignal()

    resumePreviousImport = pyqtSignal()

    def ask_resume(self):
        self.resumePreviousImport.emit()

    @pyqtSlot(int)
    @pyqtSlot(int, int)
    def sendAction(self, action, payload=None):
        self.handle_action(action, payload)

    def handle_action(self, action, payload):
        user_action = UserAction(ActionType(action), payload)
        user_action.payload = payload
        self.adapter.handle_action(user_action)

    @pyqtSlot(QUrl)
    def startSession(self, path):
        # FIXME This QThreading seems to be redundant since actual beets
        # processing is moved to a python thread to be able to wait for Events
        pathstr = path.toLocalFile()
        worker = Worker(
            self.start_session,
            pathstr
        )
        worker.signals.finished.connect(self.thread_complete)
        self._threadpool.start(worker)

    def start_session(self, path: str):
        logger.info(f"Starting import session with path: {path}")
        if config['import']['log'].get() is not None:
            logpath = config['import']['log'].as_filename()
            try:
                loghandler = logging.FileHandler(logpath)
            except IOError:
                raise UserError(
                    f"Could not open log file for writing: {logpath}")
        else:
            loghandler = None

        session = TurnipImporter(
            self._lib,
            loghandler,
            [path],
            None,
            self.adapter
        )
        session.start()

    def thread_complete(self):
        logger.info("Thread completed. Ending session")
        self.endSession.emit()


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            print("starting work")
            result = self.fn(*self.args, **self.kwargs)
        except Exception:  # TODO Stop catching every exception
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
