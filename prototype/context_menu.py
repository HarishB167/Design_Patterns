from .component import Component
from .circle import Circle

class ContextMenu:

    def duplicate(self, component: Component):
        target = component.clone()

