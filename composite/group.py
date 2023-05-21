from typing import List
from .component import Component

class Group(Component):

    def __init__(self) -> None:
        self.components: List[Component] = []

    def add(self, component: Component):
        self.components.append(component)

    def render(self):
        for component in self.components:
            component.render()

    def move(self):
        for component in self.components:
            component.move()

    