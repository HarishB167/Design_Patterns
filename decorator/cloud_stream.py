from .stream import Stream

class CloudStream(Stream):

    def write(self, data: str):
        print("Storing ", data)