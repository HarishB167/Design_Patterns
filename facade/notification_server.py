from .auth_token import AuthToken
from .connection import Connection
from .message import Message

class NotificationServer:

    def connect(self, ip_address:str) -> Connection:
        return Connection()

    def authenticate(self, appId: str, key: str) -> AuthToken:
        return AuthToken()

    def send(self, auth_token: AuthToken, message: Message, target: str):
        print("Sending a message")
