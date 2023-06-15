from .component import Component
from .timeline import Timeline

class ContextMenu:
    __timeline: Timeline = None

    def __init__(self, timeline: Timeline) -> None:
        self.__timeline = timeline

    def duplicate(self, component: Component):
        self.__timeline.add(component.clone())
