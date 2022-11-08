from .image_storage import ImageStorage
from .compressors import JpegCompressor
from .filters import BlackAndWhiteFilter

if __name__ == "__main__":
    image_storage = ImageStorage(
            JpegCompressor(), BlackAndWhiteFilter())
    image_storage.store("a")
