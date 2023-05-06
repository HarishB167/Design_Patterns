from .dialog_box import DialogBox
from .ui_control import UIControl

class Button(UIControl):
    __is_enabled: bool = False

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def is_enabled(self) -> bool:
        return self.__is_enabled

    def set_enabled(self, is_enabled: bool):
        self.__is_enabled = is_enabled
        self._owner.changed(self)

