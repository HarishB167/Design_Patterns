from .stream import Stream

class CompressedCloudStream(Stream):
    def __init__(self, stream) -> None:
        self.stream: Stream = stream

    def write(self, data: str):
        compressed = self.compress(data)
        self.stream.write(compressed)

    def compress(self, data) -> str:
        return data[:4]
        