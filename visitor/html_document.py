from typing import List
from .operation import Operation
from .html_node import HtmlNode


class HtmlDocument:

    def __init__(self) -> None:
        self.__nodes: List[HtmlNode] = []

    def add(self, node: HtmlNode):
        self.__nodes.append(node)

    def execute(self, operation: Operation):
        for node in self.__nodes:
            node.execute(operation)
            