from .component import Component

class Text(Component):
    __content: str = ""

    def __init__(self, content: str) -> None:
        self.__content = content
        
    def get_content(self) -> str:
        return self.__content

    def clone(self):
        return Text(self.__content)