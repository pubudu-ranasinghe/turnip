from beets.ui import UserError
from beets import config, logging
from turnipimporter import TurnipImportSession, Item
from PyQt5.QtCore import pyqtSignal, pyqtSlot, pyqtProperty, QUrl
from PyQt5.QtCore import QObject, QThreadPool, QRunnable
import traceback
import sys
import logging as logger


# ImportHandler class exposed to QML
class ImportHandler(QObject):
    """
    Responsible for updating the UI and responding to user input
    and communicating back and forth with `TurnipImportSession`.
    """

    _current_item: Item
    _loading_status = False

    def __init__(self, beets):
        QObject.__init__(self)
        self._threadpool = QThreadPool()
        self._lib = beets.lib
        logger.debug(f"Max {self._threadpool.maxThreadCount()} threads.")
        self._current_item = Item("path")

    # Setup qt properties
    # ===================

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

    @pyqtSlot()
    def nextValue(self):
        self._session.next_value()

    @pyqtSlot(QUrl)
    def startSession(self, path):
        # FIXME This QThreading seems to be redundant since actual beets
        # processing is moved to a python thread to be able to wait for Events
        pathstr = path.toLocalFile()
        worker = Worker(
            self.start_session,
            pathstr
        )
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        self._threadpool.start(worker)

    def start_session(self, path: str):
        logger.info(f"Starting logging session with path: {path}")
        if config['import']['log'].get() is not None:
            logpath = config['import']['log'].as_filename()
        try:
            loghandler = logging.FileHandler(logpath)
        except IOError:
            raise UserError(f"could not open log file for writing: {logpath}")
        else:
            loghandler = None

        self.set_current_item(Item("my path"))

        self._session = TurnipImportSession(
            self._lib,
            loghandler,
            [path],
            None
        )
        self._session.set_callback(self.set_current_item)
        self._session.set_loading_callback(self.set_loading_status)
        self._session.start()

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")


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
