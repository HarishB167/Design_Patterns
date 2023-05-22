from .image import Image
from .filter import Filter

class VividFilter(Filter):

    def apply(self, image: Image):
        print("Applying vivid filter")