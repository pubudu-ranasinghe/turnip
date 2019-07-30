from beets.autotag import AlbumMatch, TrackMatch
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
    elif isinstance(c, TrackMatch):
        return Candidate(
            title=c.info.title,
            artist=c.info.artist,
            year=None,
            distance=c.distance.distance
        )
    else:
        return None


# TODO Above and below are redundant
# This function is here because we are resusing the same Candidate model for
# displaying duplicates. Consider merging these models to single model that
# can hold any info(Album, Track, DB Item etc) needed to be displayed in UI
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
    if isinstance(model, TrackMatch):
        return Candidate(
            title=model.info.title,
            artist=model.info.artist,
            year=None
        )
