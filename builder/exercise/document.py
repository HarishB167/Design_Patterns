from typing import List
from .element import Element
from .document_builder import DocumentBuilder


class Document:
    __elements: List[Element] = []

    def add(self, element: Element):
        self.__elements.append(element)

    
    def export(self, builder: DocumentBuilder, file_name: str):
        for element in self.__elements:
            builder.add(element)
        builder.export_to_file(file_name)