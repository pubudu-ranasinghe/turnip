from typing import Callable
from threading import Event
from models import ImportEvent, UserAction


class ImportAdapter(object):
    """
    Consumes ImportEvents calling supplied callback fns
    and waits for the next UserAction which is returned
    TODO Don't wait indefinitely. Abort after timeout
    """
    _next_action = None
    _event_callback = None

    def __init__(self):
        self._ready = Event()

    def on_event(self, handler: Callable[[ImportEvent], bool]):
        """
        Set the callback for events
        """
        self._event_callback = handler

    def handle_action(self, action: UserAction):
        """
        Unblocks the thread waiting for UserAction
        """
        self._next_action = action
        self._ready.set()

    def consume_event(self, event: ImportEvent) -> UserAction:
        """
        Consume an event by sending it to registered event handler
        and blocks the thread until next UserAction is sent.
        """
        result = None

        if self._event_callback is not None:
            self._event_callback(event)

        self._ready.clear()
        self._ready.wait()

        if self._next_action is not None:
            result = self._next_action
            self._next_action = None

        return result
