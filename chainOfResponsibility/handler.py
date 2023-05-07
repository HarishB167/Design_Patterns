from .http_request import HttpRequest

class Handler:

    def __init__(self, next: "Handler") -> None:
        self.__next: Handler = next

    def handle(self, request: HttpRequest):
        if self.do_handle(request):
            return

        if self.__next:
            self.__next.handle(request)
    
    def do_handle(self, request: HttpRequest) -> bool:
        pass