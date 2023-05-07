from .handler import Handler
from .http_request import HttpRequest

class Authenticator(Handler):

    def __init__(self, next: "Handler") -> None:
        super().__init__(next)

    def do_handle(self, request: HttpRequest) -> bool:
        isValid = request.get_username() == "admin" and request.get_password() == "1234"
        print("Authentication : " + str(isValid))
        return (not isValid)
    