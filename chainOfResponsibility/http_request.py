
class HttpRequest:

    def __init__(self, username: str, password: str) -> None:
        self.__username: str = username
        self.__password: str = password

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password
        