from .compressor_interface import CompressorInterface

class JpegCompressor(CompressorInterface):
    def compress(self, fileName):
        print("Compressing using JPEG")


class PngCompressor(CompressorInterface):
    def compress(self, fileName):
        print("Compressing using PNG")
