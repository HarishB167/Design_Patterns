from .compressor import Compressor
from .logger import Logger
from .authenticator import Authenticator
from .web_server import WebServer
from .http_request import HttpRequest

if __name__ == "__main__":
    compressor = Compressor(None)
    logger = Logger(compressor)
    authenticator = Authenticator(logger)
    server = WebServer(authenticator)

    server.handle(HttpRequest("admin", "1234"))