from .document import Document
from .html_builder import HtmlBuilder
from .image import Image
from .text import Text
from .text_builder import TextBuilder

if __name__ == "__main__":
    document = Document()
    document.add(Text("Hello World"))
    document.add(Image("pic1.jpg"))

    document.export(HtmlBuilder(), "export.html")

    # Only writes the text elements to the file
    document.export(TextBuilder(), "export.txt")
    