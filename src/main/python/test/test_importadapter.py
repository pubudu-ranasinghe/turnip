from turnip.importadapter import ImportAdapter
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def adapter():
    return ImportAdapter()


def test_consume_event_calls_callback(adapter: ImportAdapter):
    cb = MagicMock()
    adapter.on_event(cb)
    adapter.consume_event()
    cb.assert_called_once()


def test_consume_event_returns(adapter: ImportAdapter):
    event = None
    result = adapter.consume_event(event)
    assert type(result) == "result type"
