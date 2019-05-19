import sys

from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, QThreadPool
from beet import BeetsFacade
from config import ConfigHandler
from library import LibraryHandler
from importhandler import ImportHandler


class AppContext(ApplicationContext):
    """
    Creates application context and start QML view.
    """

    def __init__(self):
        self.app.setApplicationName("Turnip")
        self.app.setOrganizationName("Turnip")
        self.app.setOrganizationDomain("com.pubuduranasinghe.turnip")

    @cached_property
    def beets(self):
        return BeetsFacade()

    @cached_property
    def config(self):
        return ConfigHandler(self.beets)

    @cached_property
    def library(self):
        return LibraryHandler(self.beets)

    @cached_property
    def importer(self):
        return ImportHandler(self.beets, self.threadpool)

    @cached_property
    def threadpool(self):
        return QThreadPool()

    def run(self):
        url = QUrl.fromLocalFile(self.get_resource("main.qml"))
        engine = QQmlApplicationEngine()

        engine.rootContext().setContextProperty("config", self.config)
        engine.rootContext().setContextProperty("library", self.library)
        engine.rootContext().setContextProperty("importer", self.importer)
        engine.load(url)

        if not engine.rootObjects():
            return -1

        return self.app.exec_()


if __name__ == '__main__':
    APP_CTXT = AppContext()

    # path = QUrl().fromLocalFile("D:/Movies/MUSIC/Akon/Akon - In My Ghetto")
    # try:
    #     print(path.toLocalFile())
    #     import_files(APP_CTXT.beets.lib, [path.toLocalFile()], None)
    # except UserError as error:
    #     print(error)
    # except Exception as error:
    #     print(error)

    EXIT_CODE = APP_CTXT.run()
    sys.exit(0)
