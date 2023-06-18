from typing import List
from .element import Element
from .export_format import ExportFormat
from .text import Text
from .image import Image
from .html.html_document import HtmlDocument
from .html.html_paragraph import HtmlParagraph
from .html.html_image import HtmlImage


class Document:
    __elements: List[Element] = []

    def add(self, element: Element):
        self.__elements.append(element)

    def export(self, format: ExportFormat, file_name: str):
        content: str = ""

        if format == ExportFormat.HTML:
            document = HtmlDocument()

            for element in self.__elements:
                if isinstance(element, Text):
                    text: Text = element.get_content()
                    document.add(HtmlParagraph(text))
                elif isinstance(element, Image):
                    source = element.get_source()
                    document.add(HtmlImage(source))
            content = str(document)

        elif format == ExportFormat.TEXT:
            string = ""

            for element in self.__elements:
                if isinstance(element, Text):
                    text = element.get_content()
                    string += text

            content = string

        with open(file_name, "w") as writer:
            writer.write(content)