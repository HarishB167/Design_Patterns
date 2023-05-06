from .data_source import DataSource
from .observer import Observer


class Chart(Observer):
    __data_source: DataSource = None

    def __init__(self, data_source) -> None:
        self.__data_source = data_source
        
    def update(self):
        print("Chart got updated: " + str(self.__data_source.get_value()))