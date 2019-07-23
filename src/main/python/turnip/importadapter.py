from typing import Callable
from enum import Enum


class EventType(Enum):
    ASK_RESUME = 1


class ActionType(Enum):
    RESUME_YES = 1
    RESUME_NO = 2


class ImportEvent(object):
    def __init__(self, e_type: EventType, payload):
        self.event_type = e_type
        self.payload = payload


class UserAction(object):
    def __init__(self, a_type: ActionType, payload):
        self.action_type = a_type
        self.payload = payload


class ImportAdapter(object):
    def __init__(self):
        pass

    # Sets the callback for events
    def on_event(self, handler: Callable[[ImportEvent], bool]):
        raise NotImplementedError

    def handle_action(self, action: UserAction):
        raise NotImplementedError

    def consume_event(self, event: ImportEvent) -> UserAction:
        raise NotImplementedError
