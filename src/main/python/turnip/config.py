from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl


class ConfigHandler(QObject):

    def __init__(self, beets_facade):
        QObject.__init__(self)
        self.__beets = beets_facade
        self.__library_path = self.__beets.get_config_value("directory")
        self.__is_copy = True

    # Configuration Path
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

    # Copy Files Configuration
    isCopyChanged = pyqtSignal(bool)

    @pyqtSlot(bool)
    def setIsCopy(self, val):
        self.set_is_copy(val)

    def set_is_copy(self, val):
        self.__is_copy = val
        if val is True:
            self.__beets.set_config_value("import.copy", True)
            self.__beets.set_config_value("import.move", False)
        else:
            self.__beets.set_config_value("import.copy", False)
            self.__beets.set_config_value("import.move", True)
        self.isCopyChanged.emit(val)

    def get_is_copy(self):
        return self.__is_copy

    isCopy = pyqtProperty(bool, get_is_copy, set_is_copy, notify=isCopyChanged)
