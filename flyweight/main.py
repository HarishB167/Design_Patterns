from .point_icon_factory import PointIconFactory
from .point_service import PointService

if __name__ == "__main__":
    service = PointService(PointIconFactory())
    for point in service.get_points():
        point.draw()