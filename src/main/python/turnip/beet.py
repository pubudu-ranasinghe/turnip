from beets.ui import _setup, human_bytes, human_seconds
from beets import config


class BeetsFacade(object):
    def __init__(self):
        subcommands, plugins, lib = _setup({})
        self.library = lib
        config.resolve()

    def getStats(self):
        items = self.library.items()

        total_size = 0
        total_time = 0.0
        total_items = 0

        for item in items:
            total_size += int(item.length * item.bitrate / 8)
            total_time += item.length
            total_items += 1

        size_str = human_bytes(total_size)
        time_str = human_seconds(total_time)
        return size_str, time_str, total_items

    def get_config_path(self):
        return config.user_config_path()

    def get_config_value(self, key):
        return config[key].as_str()

    # TODO This strips the comments in the YAML file.
    # Would be better if we can preserve the comments
    def set_config_value(self, key, value):
        config[key] = value
        updated_config = config.dump(False)
        with open(self.get_config_path(), "w") as writer:
            writer.write(updated_config)
            return True
