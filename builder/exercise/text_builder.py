from .document_builder import DocumentBuilder
from .element import Element
from .text import Text


class TextBuilder(DocumentBuilder):
    __content: str = None

    def __init__(self) -> None:
        self.__content = ""

    def add(self, element: Element):
        if isinstance(element, Text):
            text = element.get_content()
            self.__content += text

    def get_text_document(self) -> str:
        return self.__content

    def export_to_file(self, file_name: str):
        with open(file_name, "w") as writer:
            writer.write(self.__content)

