from .html_node import HtmlNode

class HeadingNode(HtmlNode):

    def execute(self, operation: "Operation"):
        operation.apply(self)
