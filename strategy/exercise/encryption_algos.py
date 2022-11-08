from .encryption_algo_interface import EncryptionAlgoInterface


class DESEncryption(EncryptionAlgoInterface):
    def encrypt(self, message):
        print("Encrypting message using DES")
        

class AESEncryption(EncryptionAlgoInterface):
    def encrypt(self, message):
        print("Encrypting message using AES")
