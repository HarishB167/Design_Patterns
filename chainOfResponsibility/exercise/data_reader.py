from .handler import Handler
from .file import File

class DataReader:

    def __init__(self, handler: Handler) -> None:
        self.__handler = handler

    def handle(self, file: File):
        self.__handler.handle(file)
