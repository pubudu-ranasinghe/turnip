from beets.importer import ImportSession, ImportTask, action
from importadapter import ImportAdapter, ImportEvent, EventType, ActionType


class TurnipImporter(ImportSession):
    def __init__(self, lib, loghandler, paths, query, adapter: ImportAdapter):
        super(TurnipImporter, self).__init__(lib, loghandler, paths, query)
        self._adapter = adapter

    def should_resume(self, path) -> bool:
        raise NotImplementedError

    def choose_item(self, task):
        raise NotImplementedError

    def choose_match(self, task: ImportTask):
        event = ImportEvent(EventType.ASK_ALBUM, "Album")
        result = self._adapter.consume_event(event)
        if result.action_type is ActionType.SKIP:
            return action.SKIP
        else:
            raise NotImplementedError

    def resolve_duplicate(self, task, found_duplicates):
        raise NotImplementedError

    def start(self):
        self.run()
