from typing import List
from .observer import Observer

class UIControl:

    def __init__(self) -> None:
        self.__observers: List[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()
