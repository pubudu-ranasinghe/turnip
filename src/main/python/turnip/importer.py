from beets.importer import ImportSession, ImportTask
from turnip.importadapter import ImportAdapter


class TurnipImporter(ImportSession):
    def __init__(self, lib, loghandler, paths, query, adapter: ImportAdapter):
        super(TurnipImporter, self).__init__(lib, loghandler, paths, query)
        self._adapter = adapter

    def should_resume(self, path) -> bool:
        raise NotImplementedError

    def choose_item(self, task):
        raise NotImplementedError

    def choose_match(self, task: ImportTask):
        raise NotImplementedError

    def resolve_duplicate(self, task, found_duplicates):
        raise NotImplementedError
