
class Slide:
    __text: str = ""

    def get_text(self) -> str:
        return self.__text
    
    def set_text(self, text: str):
        self.__text = text

        