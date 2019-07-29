from beets.importer import (
    ImportSession,
    ImportTask,
    action,
    displayable_path,
    ImportAbort
)
from importadapter import ImportAdapter
from util import build_candidate, model_to_cadidate
from models import Item, ImportEvent, EventType, ActionType
import logging


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
        elif result.action_type is ActionType.USE_AS_IS:
            return action.ASIS
        elif result.action_type is ActionType.AS_TRACKS:
            return action.TRACKS
        # TODO Manual search
        elif result.action_type is ActionType.SEARCH:
            raise NotImplementedError
        elif result.action_type is ActionType.ABORT:
            logging.warn("User initiated abort")
            raise ImportAbort()
        else:
            print("Unkown Action Type")
            raise NotImplementedError

    def resolve_duplicate(self, task: ImportTask, found_duplicates):
        old = model_to_cadidate(found_duplicates[0])
        new = model_to_cadidate(task.match)
        event = ImportEvent(EventType.RESOLVE_DUPLICATE, [old, new])
        result = self._adapter.consume_event(event)

        if result.action_type is ActionType.REPLACE_OLD:
            task.should_remove_duplicates = True
        elif result.action_type is ActionType.SKIP_NEW:
            task.set_choice(action.SKIP)
        elif result.action_type is ActionType.KEEP_BOTH:
            pass
        elif result.action_type is ActionType.MERGE:
            task.should_merge_duplicates = True
        elif result.action_type is ActionType.ABORT:
            logging.warn("User initiated abort")
            raise ImportAbort()
        else:
            print("Unkown Action Type")
            raise NotImplementedError

    def start(self):
        self.run()
