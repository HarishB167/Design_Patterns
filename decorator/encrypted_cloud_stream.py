from .stream import Stream

class EncryptedCloudStream(Stream):
    def __init__(self, stream: str) -> None:
        self.stream: Stream = stream

    def write(self, data: str):
        encrypted = self.encrypt(data)
        self.stream.write(encrypted)

    def encrypt(self, data: str) -> str:
        return "!#$#@%$#$%^#$"