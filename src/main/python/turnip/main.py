import sys

from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from beet import BeetsFacade
from config import ConfigHandler


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

    def run(self):
        url = QUrl.fromLocalFile(self.get_resource("main.qml"))
        engine = QQmlApplicationEngine()

        engine.rootContext().setContextProperty("config", self.config)
        engine.load(url)

        if not engine.rootObjects():
            return -1

        return self.app.exec_()


if __name__ == '__main__':
    APP_CTXT = AppContext()
    EXIT_CODE = APP_CTXT.run()
    sys.exit(EXIT_CODE)
