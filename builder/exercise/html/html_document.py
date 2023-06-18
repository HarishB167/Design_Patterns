from typing import List
from .html_element import HtmlElement


class HtmlDocument:
    __elements: List[HtmlElement] = []

    def add(self, element: HtmlElement):
        self.__elements.append(element)

    def __str__(self) -> str:
        string = ""
        string += "<html>"
        for element in self.__elements:
            string += str(element)
        string += "</html>"
        return string


