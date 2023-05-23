from .marker import Marker


class ErrorMarker(Marker):

    def __init__(self, marker: Marker) -> None:
        self.marker: Marker = marker

    def render(self) -> str:
        marker =  self.marker.render()
        return f"{marker} [Error]"


