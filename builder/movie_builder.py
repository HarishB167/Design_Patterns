from .movie import Movie
from .presentation_builder import PresentationBuilder
from .slide import Slide

class MovieBuilder(PresentationBuilder):
    __movie: Movie = None

    def __init__(self) -> None:
        self.__movie = Movie()

    def add_slide(self, slide: Slide):
        self.__movie.add_frame(slide.get_text(), 3)

    def get_movie(self) -> Movie:
        return self.__movie
