from .marker import Marker

class Artifact:

    def __init__(self, name: str) -> None:
        self.name:str = name

    def render(self):
        return f"{self.name}"
