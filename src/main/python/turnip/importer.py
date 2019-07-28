from beets.importer import ImportSession, ImportTask, action, displayable_path
from importadapter import ImportAdapter
from util import build_candidate
from models import Item, ImportEvent, EventType, ActionType


class TurnipImporter(ImportSession):
    def __init__(self, lib, loghandler, paths, query, adapter: ImportAdapter):
        super(TurnipImporter, self).__init__(lib, loghandler, paths, query)
        self._adapter = adapter

    def should_resume(self, path) -> bool:
        raise NotImplementedError

    def choose_item(self, task):
        raise NotImplementedError

    def choose_match(self, task: ImportTask):
        item_path = displayable_path(task.paths, " / ")
        item = Item(item_path)
        item.candidates = list(map(build_candidate, task.candidates))

        event = ImportEvent(EventType.ASK_ALBUM, item)
        result = self._adapter.consume_event(event)

        if result.action_type is ActionType.SKIP:
            return action.SKIP
        elif result.action_type is ActionType.SELECT_CANDIDATE:
            return task.candidates[result.payload]
        else:
            print("Unkown Action Type")
            raise NotImplementedError

    def resolve_duplicate(self, task, found_duplicates):
        raise NotImplementedError

    def start(self):
        self.run()
