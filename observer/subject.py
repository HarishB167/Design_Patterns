from typing import List
from .observer import Observer

class Subject:
    __observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()
