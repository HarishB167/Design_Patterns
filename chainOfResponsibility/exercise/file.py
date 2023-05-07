
class File:

    def __init__(self, file_path: str) -> None:
        self.__file_path: str = file_path

    def ends_with(self, extension: str) -> bool:
        return self.__file_path.endswith(extension)

        