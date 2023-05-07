from .handler import Handler
from .http_request import HttpRequest

class WebServer:

    def __init__(self, handler: Handler) -> None:
        self.__handler = handler

    def handle(self, request: HttpRequest):
        self.__handler.handle(request)
