from typing import List
from .document_builder import DocumentBuilder
from .element import Element
from .image import Image
from .text import Text


class Document:
    __elements: List[Element] = []

    def add(self, element: Element):
        self.__elements.append(element)

    
    def export(self, builder: DocumentBuilder, file_name: str):
        for element in self.__elements:
            if isinstance(element, Text):
                builder.add_text(element)
            elif isinstance(element, Image):
                builder.add_image(element)

        with open(file_name, "w") as writer:
            writer.write(builder.get_result())
            