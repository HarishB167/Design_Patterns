

class ConfigManager:
    __settings :dict = None
    __instance: "ConfigManager" = None

    # Suppose private constructor
    def __init__(self) -> None:
        self.__settings = {}

    @classmethod
    def get_instance(cls) -> "ConfigManager":
        if cls.__instance is None:
            cls.__instance = ConfigManager()
        return cls.__instance

    def set(self, key: str, value: object):
        self.__settings[key] = value

    def get(self, key: str) -> object:
        return self.__settings.get(key)

