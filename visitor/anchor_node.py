from .html_node import HtmlNode

class AnchorNode(HtmlNode):

    def execute(self, operation: "Operation"):
        operation.apply(self)
