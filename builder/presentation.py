from typing import List

from builder.movie import Movie

from .pdf_document import PdfDocument
from .slide import Slide
from .presentation_format import PresentationFormat

class Presentation:
    __slides: List[Slide] = []

    def add_slide(self, slide: Slide):
        self.__slides.append(slide)

    def export(self, format: PresentationFormat):
        if format == PresentationFormat.PDF:
            pdf = PdfDocument()
            pdf.add_page("Copyright")
            for slide in self.__slides:
                pdf.add_page(slide.get_text())

        elif format == PresentationFormat.MOVIE:
            movie = Movie()
            movie.add_frame("Copyright", 3)
            for slide in self.__slides:
                movie.add_frame(slide.get_text(), 3)
