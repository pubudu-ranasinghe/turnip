from typing import List
from enum import Enum


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


class EventType(Enum):
    TEST_EVENT = 1
    ASK_ALBUM = 2


class ActionType(Enum):
    UNKOWN = 0
    RESUME_YES = 1
    RESUME_NO = 2
    SKIP = 3
    SELECT_CANDIDATE = 4
    ABORT = 5


class ImportEvent(object):
    def __init__(self, e_type: EventType, payload):
        self.event_type = e_type
        self.payload = payload


class UserAction(object):
    def __init__(self, a_type: ActionType, payload):
        self.action_type = a_type
        self.payload = payload
