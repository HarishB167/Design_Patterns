from .point_type import PointType


class PointIcon:

    def __init__(self, type: PointType, icon: bytearray) -> None:
        self.type :PointType = type
        self.icon :bytearray = icon

    def get_type(self):
        return self.type
