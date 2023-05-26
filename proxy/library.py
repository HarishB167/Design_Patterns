from .ebook import Ebook

class Library:

    def __init__(self) -> None:
        self.__ebooks = {}

    def add(self, ebook: Ebook):
        self.__ebooks[ebook.get_file_name()] = ebook

    def open_ebook(self, file_name: str):
        self.__ebooks[file_name].show()
        