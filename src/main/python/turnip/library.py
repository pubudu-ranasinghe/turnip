from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty


class LibraryHandler(QObject):

    def __init__(self, beets_facade):
        QObject.__init__(self)
        self.__beets = beets_facade

        self.__stats = {}

        self.__stats["trackCount"] = beets_facade.stats["count"]
        self.__stats["totalTime"] = beets_facade.stats["time"]
        self.__stats["totalSize"] = beets_facade.stats["size"]
        self.__stats["artists"] = beets_facade.stats["artists"]
        self.__stats["albums"] = beets_facade.stats["albums"]
        self.__stats["albumArtists"] = beets_facade.stats["album_artists"]

    # Stats
    statsChanged = pyqtSignal(dict)

    def get_stats(self):
        return self.__stats

    stats = pyqtProperty("QVariantMap", get_stats, notify=statsChanged)
