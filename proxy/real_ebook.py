from .ebook import Ebook

class RealEbook(Ebook):
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name
        self.load()

    def load(self):
        print("Loading the ebook " + self.file_name)

    def show(self):
        print("Showing the ebook " + self.file_name)

    def get_file_name(self) -> str:
        return self.file_name
        