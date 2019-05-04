import sys

from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl


class AppContext(ApplicationContext):
    """
    Creates application context and start QML view.
    """

    def run(self):
        url = QUrl.fromLocalFile(self.get_resource("main.qml"))
        engine = QQmlApplicationEngine()
        engine.load(url)

        if not engine.rootObjects():
            return -1

        return self.app.exec_()


if __name__ == '__main__':
    APP_CTXT = AppContext()
    EXIT_CODE = APP_CTXT.run()
    sys.exit(EXIT_CODE)
