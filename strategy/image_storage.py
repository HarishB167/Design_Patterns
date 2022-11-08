from logging import Filter
from .compressor_interface import CompressorInterface
from .compressors import JpegCompressor, PngCompressor
from .filter_interface import FilterInterface
from .filters import BlackAndWhiteFilter

class ImageStorage:
    __compressor = None
    __filter = None

    def __init__(self, compressor: CompressorInterface, filter: FilterInterface):
        self.__compressor = compressor
        self.__filter = filter

    def store(self, fileName):
        self.__compressor.compress(fileName)
        self.__filter.apply(fileName)
        