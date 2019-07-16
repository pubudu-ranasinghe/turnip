import time
import logging
from threading import Event, Thread
from pipeline import ControlledPipeline
from beets import config
from beets.importer import ImportSession, action, ImportAbort
from beets.importer import (read_tasks,
                            group_albums,
                            log_files,
                            user_query,
                            lookup_candidates,
                            manipulate_files)

logger = logging.getLogger("turnip")
logger.setLevel(logging.DEBUG)


class Item(object):
    def __init__(self, path: str):
        self.path = path

    def to_dict(self):
        return {
            "path": self.path
        }


# ImportSession class
# class TurnipImportSession(ImportSession):
#     """An import session that runs in GUI.
#     Imports is not much documented in beets. So following is mostly based
#     on trial and error and may change in the future.

#     Imports are handled by subclassing the `ImportSession` class and
#     implementing few of the methods. A pipeline of tasks is created for
#     each item in the import path(?) and for each item one of the following
#     methods are called. Which in turn has to return a valid value based on the
#     choice of the user. As of now there doesn't seem to be a straightforward
#     way of manipulating the flow of the session.
#     """

#     want_resume = False

#     def set_callback(self, fn):
#         self._callback = fn

#     def set_config(self, pconfig):
#         self.config = pconfig

#     def choose_match(self, task):
#         logger.info(f"{len(task.items)} items")
#         item = Item(task.paths[0].decode("utf-8"))
#         print(task.paths)
#         time.sleep(1)
#         self._callback(item)
#         return action.TRACKS

#     def choose_item(self, task):
#         logger.info("choose an item")
#         time.sleep(1)
#         return action.SKIP

#     def resolve_duplicate(self, task, found_duplicates):
#         print("resolve duplicate")
#         raise NotImplementedError

#     def should_resume(self, path):
#         print(f"Import of the directory: {path} was interrupted. Resuming")
#         return True  # Always resume for now

#     def run(self):
#         logger.info("Running import session")
#         self.set_config(config['import'])

#         stages = [read_tasks(self)]

#         if self.config['pretend']:
#             stages += [log_files(self)]
#         else:
#             # stages += [group_albums(self)]
#             stages += [lookup_candidates(self), user_query(self)]
#             stages += [manipulate_files(self)]

#         pipeline = ControlledPipeline(stages)

#         try:
#             pipeline.run_sequential()
#             # for s in pipeline.run_controlled():
#             #     print(s)
#         except ImportAbort as err:
#             print("Abort Import")

class TurnipImportSession(object):
    ready = Event()

    def __init__(self, produce):
        self._produce = produce

    def next_value(self):
        print(f"received event")
        self.ready.set()

    def wait_user_input(self):
        self.ready.wait()
        return time.time()

    def start(self):
        thread = Thread(target=self.start_session)
        thread.start()

    def start_session(self):
        for i in range(5):
            print(f"{i} start work")
            print(f"{i} waiting for user")
            val = self.wait_user_input()
            self.ready.clear()
            print(f"{i} end work")
            self._produce(Item(f"Item {val}"))
    
    def some_work(self):
        print("starting long work")
        time.sleep(5)
        print("ended long work")
        return time.time()
