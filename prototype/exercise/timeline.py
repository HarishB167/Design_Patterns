from typing import List
from .component import Component


class Timeline:
    __components: List[Component] = []

    def add(self, component: Component):
        self.__components.append(component)
        