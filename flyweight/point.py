from .point_icon import PointIcon


class Point:
    def __init__(self, x: int, y: int, icon: PointIcon) -> None:
        self.x :int = x
        self.y :int = y
        self.icon :PointIcon = icon

    def draw(self, ):
        print(f"{self.icon.get_type().name} at ({self.x}, {self.y})")
