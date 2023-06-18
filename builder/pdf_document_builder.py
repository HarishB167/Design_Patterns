from .pdf_document import PdfDocument
from .presentation_builder import PresentationBuilder
from .slide import Slide

class PdfDocumentBuilder(PresentationBuilder):
    __document: PdfDocument = None

    def __init__(self) -> None:
        self.__document = PdfDocument()

    def add_slide(self, slide: Slide):
        self.__document.add_page(slide.get_text())

    def get_pdf_document(self) -> PdfDocument:
        return self.__document
        