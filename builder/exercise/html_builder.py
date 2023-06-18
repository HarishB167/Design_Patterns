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

    def add(self, element: Element):
        if isinstance(element, Text):
            text: Text = element.get_content()
            self.__document.add(HtmlParagraph(text))
        elif isinstance(element, Image):
            source = element.get_source()
            self.__document.add(HtmlImage(source))

    def get_html_document(self) -> HtmlDocument:
        return self.__document

    def export_to_file(self, file_name: str):
        with open(file_name, "w") as writer:
            writer.write(str(self.__document))
