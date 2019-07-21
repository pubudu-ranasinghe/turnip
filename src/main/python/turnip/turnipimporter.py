import logging
from threading import Event, Thread
from beets.importer import ImportSession, ImportTask, action as beets_action
from beets.autotag import AlbumMatch
from enum import Enum
from typing import List

logger = logging.getLogger("turnip")
logger.setLevel(logging.DEBUG)


class ImportActionType(Enum):
    RESUME_YES = 1
    RESUME_NO = 2
    SKIP = 3


class UserAction(object):
    """
    Action object passed from UI
    Contains the ImportActionType selected by user
    And may contain additional payload for the selected action
    """
    payload = None

    def __init__(self, type_):
        self.a_type = type_


class Candidate(object):
    distance: float
    title: str
    artist: str
    year: int

    def __init__(self, distance=None, title=None, artist=None, year=None):
        self.distance = distance
        self.title = title
        self.artist = artist
        self.year = year

    def to_dict(self):
        return {
            "distance": self.distance,
            "title": self.title,
            "artist": self.artist,
            "year": self.year
        }


class Item(object):
    candidates: List[Candidate] = []

    def __init__(self, path: str):
        self.path = path

    def to_dict(self):
        return {
            "path": self.path,
            "candidates": list(map(lambda c: c.to_dict(), self.candidates))
        }


class TurnipImportSession(ImportSession):
    ready = Event()
    user_action: UserAction

    def set_callback(self, callback):
        self._callback = callback

    def set_loading_callback(self, callback):
        self._set_loading_status = callback

    def set_ask_resume_callback(self, callback):
        self._ask_resume = callback

    def next_value(self):
        print(f"received event")
        self.ready.set()

    def wait_user_action(self):
        self._set_loading_status(False)
        self.ready.wait()
        return self.user_action

    def set_user_action(self, action: UserAction):
        self.user_action = action
        self.ready.set()

    def start(self):
        thread = Thread(target=self.run)
        thread.start()
        thread.join()

    def resolve_duplicate(self, task, found_duplicates):
        """TODO Decide what to do when a new album or item seems similar to one
        that's already in the library.
        """
        raise NotImplementedError

    def choose_match(self, task: ImportTask):
        """TODO Given an initial autotagging of items, go through an interactive
        dance with the user to ask for a choice of metadata. Returns an
        AlbumMatch object, ASIS, or SKIP.
        """
        self.ready.clear()
        # TODO Use try catch for decoding and use system encoding type
        item = Item(task.toppath.decode("UTF-8"))
        for c in task.candidates:
            if isinstance(c, AlbumMatch):
                candidate = Candidate(
                    title=c.info.album,
                    artist=c.info.artist,
                    year=c.info.year,
                    distance=c.distance.distance
                )
                item.candidates.append(candidate)
        self._callback(item)
        uaction = self.wait_user_action()
        if uaction.a_type is ImportActionType.SKIP:
            return beets_action.SKIP
        else:
            raise NotImplementedError

    def choose_item(self, task):
        """TODO Ask the user for a choice about tagging a single item. Returns
        either an action constant or a TrackMatch object.
        """
        raise NotImplementedError

    def should_resume(self, path):
        # TODO Ask the user if she wants to resume a previous import
        print('gonna resume')
        self._set_loading_status(False)
        self._ask_resume()
        print('waiting for user')
        self.wait_user_action()
        print('doone')
        return False

    def run(self):
        self._set_loading_status(True)
        super().run()
        self._set_loading_status(False)
        # TODO Emit a session end signal and move onto next screen
