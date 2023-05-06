from .dialog_box import DialogBox
from .ui_control import UIControl


class TextBox(UIControl):
    __content: str = ""

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def get_content(self) -> str:
        return self.__content

    def set_content(self, content: str):
        self.__content = content
        self._owner.changed(self)