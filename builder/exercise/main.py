from .document import Document
from .export_format import ExportFormat
from .text import Text
from .image import Image

if __name__ == "__main__":
    document = Document()
    document.add(Text("Hello World"))
    document.add(Image("pic1.jpg"))

    document.export(ExportFormat.HTML, "export.html")

    # Only writes the text elements to the file
    document.export(ExportFormat.TEXT, "export.txt")
    