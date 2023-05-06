from .subject import Subject


class DataSource(Subject):
    __value: int = 0

    def get_value(self) -> int:
        return self.__value
    
    def set_value(self, value: int):
        self.__value = value
        self.notify_observers()
