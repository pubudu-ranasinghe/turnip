from beets.ui import _setup, human_bytes, human_seconds
from beets import config


class BeetsFacade(object):
    def __init__(self):
        subcommands, plugins, lib = _setup({})
        self.library = lib
        self.stats = {}
        self.update_stats()
        config.resolve()

    def lib(self):
        return self.library

    def update_stats(self):
        items = self.library.items()

        total_size = 0
        total_time = 0.0
        total_items = 0
        artists = set()
        albums = set()
        album_artists = set()

        for item in items:
            total_size += int(item.length * item.bitrate / 8)
            total_time += item.length
            total_items += 1
            artists.add(item.artist)
            album_artists.add(item.albumartist)
            if item.album_id:
                albums.add(item.album_id)

        size_str = human_bytes(total_size)
        time_str = human_seconds(total_time)
        self.stats["count"] = total_items
        self.stats["time"] = time_str
        self.stats["size"] = size_str
        self.stats["artists"] = len(artists)
        self.stats["albums"] = len(albums)
        self.stats["album_artists"] = len(album_artists)

    def get_config_path(self):
        return config.user_config_path()

    def get_config_value(self, key):
        return config[key].as_str()

    # TODO This strips the comments in the YAML file.
    # Would be better if we can preserve the comments
    def set_config_value(self, key, value):
        # TODO
        # This is a temporary hack to set nested config values
        parts = key.split(".")
        if len(parts) > 1:
            config[parts[0]][parts[1]] = value
        else:
            config[parts[0]] = value

    def dump_config(self):
        return config.dump(False)
