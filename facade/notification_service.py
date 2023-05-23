from .notification_server import NotificationServer
from .message import Message

class NotificationService:

    def send(self, message: str, target: str):
        server = NotificationServer()
        connection = server.connect("ip")
        auth_token = server.authenticate("appID", "key")
        server.send(auth_token, Message(message), target)
        connection.disconnect()
