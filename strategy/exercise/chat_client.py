from .encryption_algo_interface import EncryptionAlgoInterface
from .encryption_algos import DESEncryption, AESEncryption


class ChatClient:
    __encryption_algorithm = None

    def __init__(self, encryption_algorithm: EncryptionAlgoInterface):
        self.__encryption_algorithm = encryption_algorithm

    def send(self, message):
        self.__encryption_algorithm.encrypt(message)
        print("Sending the encrypted message...")

