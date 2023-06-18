from .presentation import Presentation
from .slide import Slide
from .pdf_document_builder import PdfDocumentBuilder
from .movie_builder import MovieBuilder

if __name__ == "__main__":
    presentation = Presentation()
    presentation.add_slide(Slide("Slide 1"))
    presentation.add_slide(Slide("Slide 2"))

    builder = MovieBuilder()
    presentation.export(builder)
    movie = builder.get_movie()
