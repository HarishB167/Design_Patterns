from .filter import Filter
from .fact_segment import FactSegment
from .format_segment import FormatSegment

class ReverbFilter(Filter):

    def apply_fact_segment(self, segment: FactSegment):
        print("Add reverb: fact-segment")

    def apply_format_segment(self, segment: FormatSegment):
        print("Add reverb: format-segment")
        