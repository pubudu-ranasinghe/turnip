from beets.autotag import AlbumMatch
from turnip.importer import Candidate


def build_candidate(self, c):
    if isinstance(c, AlbumMatch):
        return Candidate(
            title=c.info.album,
            artist=c.info.artist,
            year=c.info.year,
            distance=c.distance.distance
        )
    else:
        return None
