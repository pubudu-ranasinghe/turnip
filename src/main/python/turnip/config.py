from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl


class ConfigHandler(QObject):

    def __init__(self, beetsFacade):
        QObject.__init__(self)
        self.__beets = beetsFacade
        self.__library_path = self.__beets.get_config_value("directory")

    configPathChanged = pyqtSignal(str)

    def get_config_path(self):
        path = QUrl().fromLocalFile(self.__beets.get_config_path())
        return path.toLocalFile()

    configPath = pyqtProperty(str, get_config_path, notify=configPathChanged)

    # Library Path
    libraryPathChanged = pyqtSignal(str)

    @pyqtSlot(QUrl)
    def setLibraryPath(self, val):
        self.set_library_path(val)

    def set_library_path(self, val):
        # TODO save library path in YAML
        if isinstance(val, QUrl):
            path = val.toLocalFile()
            self.__library_path = path
            self.__beets.set_config_value("directory", path)
            self.libraryPathChanged.emit(path)

    def get_library_path(self):
        return self.__library_path

    libraryPath = pyqtProperty(
        str,
        get_library_path,
        set_library_path,
        notify=libraryPathChanged
    )
