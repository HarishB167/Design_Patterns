from .document_builder import DocumentBuilder
from .text import Text
from .image import Image


class TextBuilder(DocumentBuilder):
    __content: str = None

    def __init__(self) -> None:
        self.__content = ""

    def add_text(self, text: Text):
        self.__content += text.get_content()

    def add_image(self, image: Image):
        pass

    def get_result(self):
        return self.__content
