from .filter import Filter
from .image import Image

class ImageView:
    def __init__(self, image: Image) -> None:
        self.image: Image = image

    def apply(self, filter: Filter):
        filter.apply(self.image)
        