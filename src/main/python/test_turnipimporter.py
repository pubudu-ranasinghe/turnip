import pytest
from turnip.turnipimporter import TurnipImportSession


def test_answer():
    assert 1+1 == 2


@pytest.fixture
def turnipimporter():
    """Returns initialized TurnipImportSession"""
    return TurnipImportSession(None, None, None, None)
