from .element import Element

class Image(Element):
    __source: str = ""

    def __init__(self, source) -> None:
        self.__source = source

    def get_source(self):
        return self.__source
        