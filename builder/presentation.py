from typing import List

from .movie import Movie
from .pdf_document import PdfDocument
from .slide import Slide
from .presentation_format import PresentationFormat
from .presentation_builder import PresentationBuilder

class Presentation:
    __slides: List[Slide] = []

    def add_slide(self, slide: Slide):
        self.__slides.append(slide)

    def export(self, builder: PresentationBuilder):
        builder.add_slide(Slide("Copyright"))
        for slide in self.__slides:
            builder.add_slide(slide)
            