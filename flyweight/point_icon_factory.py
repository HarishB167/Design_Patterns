from flyweight.point_type import PointType
from .point_icon import PointIcon

class PointIconFactory:

    def __init__(self) -> None:
        self.icons :dict = {}

    def get_point_icon(self, type:PointType):
        if type.name not in self.icons:
            icon = PointIcon(type, None)
            self.icons[type.name] = icon
        return self.icons[type.name]
