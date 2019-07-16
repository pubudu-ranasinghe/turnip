import time
import logging
from threading import Event, Thread
from beets.importer import ImportSession

logger = logging.getLogger("turnip")
logger.setLevel(logging.DEBUG)


class Item(object):
    def __init__(self, path: str):
        self.path = path

    def to_dict(self):
        return {
            "path": self.path
        }


class TurnipImportSession(ImportSession):
    ready = Event()

    def set_callback(self, callback):
        self._callback = callback

    def set_loading_callback(self, callback):
        self._set_loading_status = callback

    def next_value(self):
        print(f"received event")
        self.ready.set()

    def wait_user_input(self):
        self.ready.wait()
        return time.time()

    def start(self):
        thread = Thread(target=self.run)
        thread.start()

    def resolve_duplicate(self, task, found_duplicates):
        """TODO Decide what to do when a new album or item seems similar to one
        that's already in the library.
        """
        raise NotImplementedError

    def choose_match(self, tasl):
        """TODO Given an initial autotagging of items, go through an interactive
        dance with the user to ask for a choice of metadata. Returns an
        AlbumMatch object, ASIS, or SKIP.
        """
        raise NotImplementedError

    def choose_item(self, task):
        """TODO Ask the user for a choice about tagging a single item. Returns
        either an action constant or a TrackMatch object.
        """
        raise NotImplementedError

    def should_resume(self, path):
        # TODO Ask the user if she wants to resume a previous import
        raise NotImplementedError

    def run(self):
        self._set_loading_status(True)
        super().run()
        # TODO Emit a session end signal and move onto next screen
