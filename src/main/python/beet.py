from beets.ui import _setup, human_bytes, human_seconds


class BeetsFacade(object):
    def __init__(self):
        subcommands, plugins, lib = _setup({})
        self.library = lib

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
