
class Slide:
    __text: str = ""

    def __init__(self, text: str = "") -> None:
        self.__text = text

    def get_text(self) -> str:
        return self.__text
    
    def set_text(self, text: str):
        self.__text = text

        