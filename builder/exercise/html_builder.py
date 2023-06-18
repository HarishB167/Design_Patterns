from .document_builder import DocumentBuilder
from .element import Element
from .html.html_document import HtmlDocument
from .html.html_image import HtmlImage
from .html.html_paragraph import HtmlParagraph
from .image import Image
from .text import Text


class HtmlBuilder(DocumentBuilder):
    __document: HtmlDocument = None

    def __init__(self) -> None:
        self.__document = HtmlDocument()

    def add_text(self, text: Text):
        self.__document.add(HtmlParagraph(text.get_content()))

    def add_image(self, image: Image):
        self.__document.add(HtmlImage(image.get_source()))

    def get_result(self):
        return str(self.__document)
        