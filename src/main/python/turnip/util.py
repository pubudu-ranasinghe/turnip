from beets.autotag import AlbumMatch
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
