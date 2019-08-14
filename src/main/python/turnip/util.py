from beets.autotag import AlbumMatch, TrackMatch
from beets.library import Item, Album
from beets.util import _fsencoding
from models import Candidate


def build_candidate(c):
    if isinstance(c, AlbumMatch):
        return Candidate(
            title=c.info.album,
            artist=c.info.artist,
            year=c.info.year,
            percentage=int((1 - c.distance) * 100),
            isAlbum=True,
            albumtype=c.info.albumtype,
            label=c.info.label,
            country=c.info.country,
            media=c.info.media
        )
    elif isinstance(c, TrackMatch):
        return Candidate(
            title=c.info.title,
            artist=c.info.artist,
            year=None,
            percentage=int((1 - c.distance) * 100),
            isAlbum=False
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


def format_paths(path, toppath, separator="; "):
    """Attempts to decode a bytestring path to a unicode object for the
    purpose of displaying it to the user. If the `path` argument is a
    list or a tuple, the elements are joined with `separator`.
    """
    top_path = toppath.decode(_fsencoding(), 'ignore')

    if isinstance(path, (list, tuple)):
        return separator.join(format_paths(p, toppath) for p in path)
    elif isinstance(path, str):
        short_path = path.replace(top_path, '') if top_path in path else path
        return short_path

    try:
        decoded_path = path.decode(_fsencoding(), 'ignore')
        short_path = decoded_path.replace(
            top_path, '') if top_path in decoded_path else decoded_path
        return short_path
    except (UnicodeError, LookupError):
        decoded_path = path.decode('utf-8', 'ignore')
        short_path = decoded_path.replace(
            top_path, '') if top_path in decoded_path else decoded_path
        return short_path
