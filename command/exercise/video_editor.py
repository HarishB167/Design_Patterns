
class VideoEditor:
    __contrast: float = 0.5
    __text: str = ""

    def set_text(self, text:str):
        self.__text = text

    def remove_text(self):
        self.__text = ""

    def get_contrast(self) -> float:
        return self.__contrast

    def set_contrast(self, contrast: float):
        self.__contrast = contrast

    def __str__(self) -> str:
        return ("VideoEditor{" +
                "contrast=" + str(self.__contrast) +
                ", text='" + self.__text + '\'' +
                '}')
