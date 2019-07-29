# from turnip.importadapter import (
#     ImportAdapter, ImportEvent, UserAction, EventType, ActionType)
# from unittest.mock import MagicMock
# from threading import Timer
# from pytest import fixture


# @fixture
# def adapter():
#     return ImportAdapter()


# def test_consume_event_calls_callback(adapter: ImportAdapter):
#     cb = MagicMock()
#     event = ImportEvent(EventType.TEST_EVENT, None)
#     action = UserAction(ActionType.TEST_ACTION, None)
#     adapter.on_event(cb)
#     r = Timer(3, lambda: adapter.handle_action(action))
#     r.start()
#     adapter.consume_event(event)
#     cb.assert_called_once()


# def test_consume_event_validEvent_returnsAction(adapter: ImportAdapter):
#     event = ImportEvent(EventType.TEST_EVENT, None)
#     action = UserAction(ActionType.TEST_ACTION, None)
#     r = Timer(3, lambda: adapter.handle_action(action))
#     r.start()
#     result = adapter.consume_event(event)
#     assert type(result) is UserAction
