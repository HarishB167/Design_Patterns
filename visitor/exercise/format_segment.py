from .segment import Segment

class FormatSegment(Segment):

    def execute(self, filter: "Filter"):
        filter.apply(self)
        