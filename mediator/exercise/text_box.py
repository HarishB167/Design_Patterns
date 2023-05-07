from .ui_control import UIControl

class TextBox(UIControl):

    def __init__(self) -> None:
        super().__init__()
        self.content: str = ""

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str) -> None:
        self.content = content
        self.notify_observers()
