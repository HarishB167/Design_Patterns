from .component import Component

class Clip(Component):
    def clone(self):
        return Clip()