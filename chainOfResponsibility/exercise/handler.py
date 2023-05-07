from .file import File


class Handler:

    def __init__(self, next: "Handler") -> None:
        self.__next: Handler = next

    def handle(self, file: File):
        if file.ends_with(self.get_extension()):
            self.do_handle(file)
            return

        if self.__next:
            self.__next.handle(file)
        else:
            raise Exception("File formant not supported")

    def do_handle(self, file: File) -> bool:
        pass

    def get_extension(self) -> str:
        pass