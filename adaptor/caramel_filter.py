from .filter import Filter
from .image import Image
from .avaFilters.caramel import Caramel

class CaramelFilter(Filter):

    def __init__(self, caramel: Caramel) -> None:
        self.caramel: Caramel = caramel

    def apply(self, image: Image):
        self.caramel.init()
        self.caramel.render(image)
        