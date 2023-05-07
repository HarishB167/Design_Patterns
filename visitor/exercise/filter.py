from .fact_segment import FactSegment
from .format_segment import FormatSegment

class Filter:
    def apply(self, segment):
        if isinstance(segment, FactSegment):
            self.apply_fact_segment(segment)
        elif isinstance(segment, FormatSegment):
            self.apply_format_segment(segment)

    def apply_fact_segment(self, segment: FactSegment):
        pass

    def apply_format_segment(self, segment: FormatSegment):
        pass