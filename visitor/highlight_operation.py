from .anchor_node import AnchorNode
from .heading_node import HeadingNode
from .operation import Operation

class HighlightOperation(Operation):

    def apply_heading_node(self, nodeObj: HeadingNode):
        print("highlight-heading")
        
    def apply_anchor_node(self, nodeObj: AnchorNode):
        print("highlight-anchor")
