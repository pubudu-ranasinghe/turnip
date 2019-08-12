from typing import List
from enum import Enum


class Candidate(object):

    def __init__(self, distance=None, title=None, artist=None, year=None,
                 albumtype=None, label=None, country=None, media=None,
                 isAlbum=None):
        self.distance = distance
        self.title = title
        self.artist = artist
        self.year = year
        self.albumtype = albumtype
        self.label = label
        self.country = country
        self.media = media
        self.isAlbum = isAlbum

    def to_dict(self):
        return {
            "distance": self.distance,
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "isAlbum": self.isAlbum,
            "albumtype": self.albumtype,
            "label": self.label,
            "country": self.country,
            "media": self.media
        }


class Item(object):
    candidates: List[Candidate] = []
    is_album = True

    def __init__(self, path: str):
        self.path = path

    def to_dict(self):
        return {
            "path": self.path,
            "candidates": list(map(lambda c: c.to_dict(), self.candidates)),
            "isAlbum": self.is_album
        }


class EventType(Enum):
    TEST_EVENT = 1
    ASK_ALBUM = 2
    RESOLVE_DUPLICATE = 3
    ASK_TRACK = 4
    ASK_RESUME = 5


class ActionType(Enum):
    # Global actions
    UNKOWN = 0
    ABORT = 1
    # Resume actions
    RESUME_YES = 10
    RESUME_NO = 11
    # Track/Album match actions
    SKIP = 20
    SELECT_CANDIDATE = 21
    USE_AS_IS = 22
    AS_TRACKS = 23
    SEARCH = 24
    # Duplicate item actions
    REPLACE_OLD = 30
    SKIP_NEW = 31
    KEEP_BOTH = 32
    MERGE = 33


class ImportEvent(object):
    def __init__(self, e_type: EventType, payload):
        self.event_type = e_type
        self.payload = payload


class UserAction(object):
    def __init__(self, a_type: ActionType, payload):
        self.action_type = a_type
        self.payload = payload
