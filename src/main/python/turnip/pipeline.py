from beets.util.pipeline import Pipeline, _allmsgs


class ControlledPipeline(Pipeline):

    def test(self):
        next(self.run_controlled())

    def run_controlled(self):
        coros = [stage[0] for stage in self.stages]

        # "Prime" the coroutines.
        for coro in coros[1:]:
            next(coro)

        # Begin the pipeline.
        for out in coros[0]:
            msgs = _allmsgs(out)
            for coro in coros[1:]:
                next_msgs = []
                for msg in msgs:
                    out = coro.send(msg)
                    next_msgs.extend(_allmsgs(out))
                yield msgs
                msgs = next_msgs
