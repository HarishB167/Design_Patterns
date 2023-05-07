from .file import File
from .handler import Handler

class NumbersReader(Handler):

    def __init__(self, next: "Handler") -> None:
        super().__init__(next)

    def do_handle(self, file: File) -> None:
        print("Reading data from a Numbers spreadsheet.")

    def get_extension(self) -> str:
        return ".numbers"