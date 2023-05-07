from typing import List
from .filter import Filter
from .segment import Segment


class WavFile:

    def __init__(self) -> None:
        self.__segments: List[Segment] = []

    def add(self, segment: Segment):
        self.__segments.append(segment)

    def execute(self, filter: Filter):
        for segment in self.__segments:
            segment.execute(filter)
            
