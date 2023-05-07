from .filter import Filter
from .fact_segment import FactSegment
from .format_segment import FormatSegment

class ReduceNoiseFilter(Filter):

    def apply_fact_segment(self, segment: FactSegment):
        print("Reduce-noise: fact-segment")

    def apply_format_segment(self, segment: FormatSegment):
        print("Reduce-noise: format-segment")
        