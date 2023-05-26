from .ebook import Ebook
from .real_ebook import RealEbook

class LoggingEbookProxy(Ebook):
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name
        self.__real_ebook: Ebook = None

    def show(self):
        if not self.__real_ebook:
            self.__real_ebook = RealEbook(self.file_name)
            
        print("Logging")
        self.__real_ebook.show()

    def get_file_name(self) -> str:
        return self.file_name
        