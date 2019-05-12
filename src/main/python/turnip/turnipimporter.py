from beets import importer


# ImportSession class
class TurnipImportSession(importer.ImportSession):
    """An import session that runs in GUI.
    """
    def choose_match(self, task):
        print("{0} items".format(len(task.items)))
        raise NotImplementedError

    def choose_item(self, task):
        raise NotImplementedError

    def resolve_duplicate(self, task, found_duplicates):
        print("resolve duplicate")
        raise NotImplementedError

    def should_resume(self, path):
        print("should resume")
        raise NotImplementedError
