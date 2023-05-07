from .ui_control import UIControl


class TextBox(UIControl):
    __content: str = ""

    def get_content(self) -> str:
        return self.__content

    def set_content(self, content: str):
        self.__content = content
        self.notify_observers()