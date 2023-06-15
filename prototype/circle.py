from .component import Component

class Circle(Component):
    __radius: int = 0

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def render(self):
        print("Rendering a circe.")

    def clone(self) -> "Component":
        new_circle = Circle()
        new_circle.set_radius(self.__radius)
        return new_circle
