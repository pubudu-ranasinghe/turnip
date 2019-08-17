from beets.importer import (
    ImportSession,
    ImportTask,
    action,
    ImportAbort,
    displayable_path
)
from importadapter import ImportAdapter
from util import build_candidate, model_to_cadidate, format_paths
from models import Item, ImportEvent, EventType, ActionType
import logging


class TurnipImporter(ImportSession):
    track_count = 0

    def __init__(self, lib, loghandler, paths, query, adapter: ImportAdapter):
        super(TurnipImporter, self).__init__(lib, loghandler, paths, query)
        self._adapter = adapter

    def should_resume(self, path) -> bool:
        event = ImportEvent(EventType.ASK_RESUME, displayable_path(path))
        result = self._adapter.consume_event(event)

        if result.action_type is ActionType.RESUME_YES:
            return True
        elif result.action_type is ActionType.RESUME_NO:
            return False
        else:
            raise NotImplementedError

    # Tagging track
    def choose_item(self, task: ImportTask):
        item_path = format_paths(task.paths, task.toppath, "\n")
        item = Item(item_path)
        item.is_album = False
        item.candidates = list(map(build_candidate, task.candidates))
        item.no_match = len(item.candidates) == 0

        event = ImportEvent(EventType.ASK_TRACK, item)
        result = self._adapter.consume_event(event)

        if result.action_type is ActionType.SKIP:
            return action.SKIP
        elif result.action_type is ActionType.USE_AS_IS:
            self.track_count += 1
            return action.ASIS
        elif result.action_type is ActionType.SELECT_CANDIDATE:
            self.track_count += 1
            return task.candidates[result.payload]
            # TODO Manual search
        elif result.action_type is ActionType.SEARCH:
            raise NotImplementedError
        elif result.action_type is ActionType.ABORT:
            logging.warn("User initiated abort")
            raise ImportAbort()
        else:
            print("Unkown Action Type")
            raise NotImplementedError

    # Tagging album
    def choose_match(self, task: ImportTask):
        item_path = format_paths(task.paths, task.toppath, "\n")
        item = Item(item_path)
        item.is_album = True
        item.candidates = list(map(build_candidate, task.candidates))
        item.no_match = len(item.candidates) == 0

        event = ImportEvent(EventType.ASK_ALBUM, item)
        result = self._adapter.consume_event(event)

        if result.action_type is ActionType.SKIP:
            return action.SKIP
        elif result.action_type is ActionType.SELECT_CANDIDATE:
            self.track_count += len(task.items)
            return task.candidates[result.payload]
        elif result.action_type is ActionType.USE_AS_IS:
            self.track_count += len(task.items)
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
