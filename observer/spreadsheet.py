from .data_source import DataSource
from .observer import Observer


class Spreadsheet(Observer):
    __data_source: DataSource = None

    def __init__(self, data_source) -> None:
        self.__data_source = data_source

    def update(self):
        print("Spreadsheet got notified: " + str(self.__data_source.get_value()))