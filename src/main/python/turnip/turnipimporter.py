from beets.importer import ImportSession, action
import logging
import time

logger = logging.getLogger("turnip")
logger.setLevel(logging.DEBUG)


# ImportSession class
class TurnipImportSession(ImportSession):
    """An import session that runs in GUI.
    """

    def choose_match(self, task):
        logger.info(f"{len(task.items)} items")
        time.sleep(1)
        return action.TRACKS

    def choose_item(self, task):
        logger.info("choose an item")
        raise NotImplementedError

    def resolve_duplicate(self, task, found_duplicates):
        print("resolve duplicate")
        raise NotImplementedError

    def should_resume(self, path):
        print(f"Import of the directory: {path} was interrupted. Resuming")
        return True  # Always resume for now
