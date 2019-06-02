from beets.importer import ImportSession, action
import logging
import time

logger = logging.getLogger("turnip")
logger.setLevel(logging.DEBUG)


# ImportSession class
class TurnipImportSession(ImportSession):
    """An import session that runs in GUI.
    Imports is not much documented in beets. So following is mostly based
    on trial and error and may change in the future.

    Imports are handled by subclassing the `ImportSession` class and
    implementing few of the methods. A pipeline of tasks is created for
    each item in the import path(?) and for each item one of the following
    methods are called. Which in turn has to return a valid value based on the
    choice of the user. As of now there doesn't seem to be a straightforward
    way of manipulating the flow of the session.
    """

    want_resume = False

    def set_callback(self, fn):
        self._callback = fn

    def set_config(self, pconfig):
        self.config = pconfig

    def choose_match(self, task):
        logger.info(f"{len(task.items)} items")
        time.sleep(1)
        return action.TRACKS

    def choose_item(self, task):
        logger.info("choose an item")
        time.sleep(1)
        return action.SKIP

    def resolve_duplicate(self, task, found_duplicates):
        print("resolve duplicate")
        raise NotImplementedError

    def should_resume(self, path):
        print(f"Import of the directory: {path} was interrupted. Resuming")
        return True  # Always resume for now

    # def run(self):
    #     logger.info("Running import session")
    #     self.set_config(config['import'])
    #     stages = [read_tasks(self)]
    #     log.info(u'Album: {0}', displayable_path(task.paths[0]))
    #     next