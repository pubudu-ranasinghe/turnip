from turnip.pipeline import ControlledPipeline
from unittest.mock import MagicMock


def test_answer():
    assert 1+1 == 2


def produce():
    yield 0


def work():
    while True:
        val = yield
        yield val + 1


def consume(cb):
    while True:
        final = yield
        cb(final)


def test_pipeline_sequential():
    cb = MagicMock()
    pipeline = ControlledPipeline([
        produce(),
        work(),
        work(),
        work(),
        work(),
        consume(cb)
    ])
    pipeline.run_sequential()
    cb.assert_called_once_with(4)


def test_pipeline_parallel():
    cb = MagicMock()
    pipeline = ControlledPipeline([
        produce(),
        work(),
        work(),
        work(),
        work(),
        consume(cb)
    ])
    pipeline.run_parallel(3)
    cb.assert_called_once_with(4)
