from .anchor_node import AnchorNode
from .heading_node import HeadingNode
from .operation import Operation

class PlainTextOperation(Operation):

    def apply_anchor_node(self, nodeObj: AnchorNode):
        print("text-anchor")

    def apply_heading_node(self, nodeObj: HeadingNode):
        print("text-heading")