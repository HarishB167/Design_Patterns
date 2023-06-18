from .html_element import HtmlElement

class HtmlImage(HtmlElement):
    __source: str = ""

    def __init__(self, source) -> None:
        self.__source = source

    def __str__(self) -> str:
        return f"<img src=\"{self.__source}\" />"
        