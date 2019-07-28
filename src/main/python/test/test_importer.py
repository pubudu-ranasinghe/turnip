from pytest import fixture
from turnip.importer import TurnipImporter


@fixture
def session():
    return TurnipImporter(None, None, None, None, None)


def test_should_resume_returnsBool(session: TurnipImporter):
    result = session.should_resume(None)
    assert type(result) == bool
