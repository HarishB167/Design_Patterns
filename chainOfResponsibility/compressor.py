from .handler import Handler
from .http_request import HttpRequest

class Compressor(Handler):

    def __init__(self, next: "Handler") -> None:
        super().__init__(next)

    def do_handle(self, request: HttpRequest) -> bool:
        print("Compress")
        return False