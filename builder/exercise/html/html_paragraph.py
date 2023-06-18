from .html_element import HtmlElement

class HtmlParagraph(HtmlElement):
    __text: str = ""

    def __init__(self, text) -> None:
        self.__text = text

    def __str__(self) -> str:
        return f"<p>{self.__text}</p>"
        