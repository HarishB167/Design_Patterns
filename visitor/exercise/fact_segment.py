from .segment import Segment

class FactSegment(Segment):

    def execute(self, filter: "Filter"):
        filter.apply(self)
        