class Logger:
    __fileName: str = ""
    __instances: "Logger" = None

    def __init__(self, fileName: str) -> None:
        self.__fileName = fileName

    def write(self, message: str):
        print("Writing a message to the log.")

    @classmethod
    def get_instance(cls, fileName) -> "Logger":
        if cls.__instances is None:
            cls.__instances = {}
        if fileName not in cls.__instances:
            cls.__instances[fileName] = Logger(fileName)
        return cls.__instances.get(fileName)


