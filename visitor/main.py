from .html_document import HtmlDocument
from .heading_node import HeadingNode
from .anchor_node import AnchorNode
from .highlight_operation import HighlightOperation
from .plain_text_operation import PlainTextOperation

if __name__ == '__main__':
    document = HtmlDocument()
    document.add(HeadingNode())
    document.add(AnchorNode())
    document.execute(HighlightOperation())
    document.execute(PlainTextOperation())
