from typing import List

from .point_icon_factory import PointIconFactory
from .point_type import PointType
from .point import Point

class PointService:

    def __init__(self, icon_factory: PointIconFactory) -> None:
        self.icon_factory: PointIconFactory = icon_factory

    def get_points(self) -> List[Point]:
        points = [Point(1,2, self.icon_factory.get_point_icon(PointType.CAFE))]
        return points
