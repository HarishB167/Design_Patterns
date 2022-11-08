from .chat_client import ChatClient
from .encryption_algos import AESEncryption


if __name__ == "__main__":
    client = ChatClient(AESEncryption())
    client.send("some message")
    