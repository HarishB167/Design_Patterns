from .heading_node import HeadingNode
from .anchor_node import AnchorNode

class Operation:
    def apply(self, nodeObj):
        if isinstance(nodeObj, HeadingNode):
            self.apply_heading_node(nodeObj)
        elif isinstance(nodeObj, AnchorNode):
            self.apply_anchor_node(nodeObj)

    def apply_heading_node(self, nodeObj: HeadingNode):
        pass

    def apply_anchor_node(self, nodeObj: AnchorNode):
        pass