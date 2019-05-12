import os
from beets.ui import UserError
from beets import config, logging
from turnipimporter import TurnipImportSession
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl


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

    def __init__(self, beets_facade):
        QObject.__init__(self)
        self.__beets = beets_facade

    @pyqtSlot()
    def start(self):
        print("Starting")
