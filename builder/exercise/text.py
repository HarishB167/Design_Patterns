from .element import Element

class Text(Element):
    __content: str = ""

    def __init__(self, content: str) -> None:
        self.__content = content

    def get_content(self) -> str:
        return self.__content
        