from beets.autotag import AlbumMatch
from beets.library import Item, Album
from models import Candidate


def build_candidate(c):
    if isinstance(c, AlbumMatch):
        return Candidate(
            title=c.info.album,
            artist=c.info.artist,
            year=c.info.year,
            distance=c.distance.distance
        )
    else:
        return None


def model_to_cadidate(model):
    if isinstance(model, Album):
        return Candidate(
            title=model.album,
            artist=model.albumartist,
            year=model.year
        )
    if isinstance(model, Item):
        return Candidate(
            title=model.title,
            artist=model.artist,
            year=model.year
        )
    if isinstance(model, AlbumMatch):
        return Candidate(
            title=model.info.album,
            artist=model.info.artist,
            year=model.info.year
        )
