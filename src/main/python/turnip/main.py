import sys
from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtCore import QUrl, QObject, Q_ENUM
from beet import BeetsFacade
from confighandler import ConfigHandler
from library import LibraryHandler
from importhandler import ImportHandler
from importadapter import ImportAdapter
from models import ActionType


class QActionType(QObject):
    """
    Wrapped ActionType Enum exposed to QML
    """
    Q_ENUM(ActionType)


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
    def adapter(self):
        return ImportAdapter()

    @cached_property
    def importer(self):
        return ImportHandler(self.beets, self.adapter)

    def run(self):
        url = QUrl.fromLocalFile(self.get_resource("main.qml"))
        engine = QQmlApplicationEngine()

        qmlRegisterType(QActionType, "ActionType", 1, 0, "ActionType")

        engine.rootContext().setContextProperty("config", self.config)
        engine.rootContext().setContextProperty("library", self.library)
        engine.rootContext().setContextProperty("importer", self.importer)
        engine.load(url)

        if not engine.rootObjects():
            return -1

        return self.app.exec_()


if __name__ == '__main__':
    APP_CTXT = AppContext()
    EXIT_CODE = APP_CTXT.run()
    sys.exit(EXIT_CODE)
