import os
from beets.ui import UserError
from beets import config, logging
from turnipimporter import TurnipImportSession
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl, QRunnable
import traceback
import sys
import logging as logger


def import_files(lib, paths, query):
    for path in paths:
        if not os.path.exists(path):
            raise UserError('no such file or directory:{0}'.format(path))

    if config['import']['quiet'] and config['import']['timid']:
        raise UserError(u"can't be both quiet and timid")

    if config['import']['log'].get() is not None:
        logpath = config['import']['log'].as_filename()
        try:
            loghandler = logging.FileHandler(logpath)
        except IOError:
            raise UserError(u"could not open log file for writing: "
                            u"{0}".format(logpath))
    else:
        loghandler = None

    session = TurnipImportSession(lib, loghandler, paths, query)
    session.run()

    # Emit plugin event


# ImportHandler class exposed to QML
class ImportHandler(QObject):

    def __init__(self, beets, threadpool):
        QObject.__init__(self)
        self._threadpool = threadpool
        self._lib = beets.lib
        logger.debug(f"Max {self._threadpool.maxThreadCount()} threads.")

    @pyqtSlot(QUrl)
    def startSession(self, path):
        pathstr = path.toLocalFile()
        worker = Worker(self.start_session, pathstr)
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

        session = TurnipImportSession(self._lib, loghandler, [path], None)
        session.run()

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
