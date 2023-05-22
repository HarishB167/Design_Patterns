from .image_view import ImageView
from .image import Image
from .vivid_filter import VividFilter
from .caramel_filter import CaramelFilter
from .avaFilters.caramel import Caramel

if __name__ == '__main__':
    image_view = ImageView(Image())
    image_view.apply(CaramelFilter(Caramel()))
    