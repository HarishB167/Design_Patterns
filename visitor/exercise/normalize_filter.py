from .filter import Filter
from .fact_segment import FactSegment
from .format_segment import FormatSegment

class NormalizeFilter(Filter):

    def apply_fact_segment(self, segment: FactSegment):
        print("Normalize: fact-segment")

    def apply_format_segment(self, segment: FormatSegment):
        print("Normalize: format-segment")
        