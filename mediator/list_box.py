from .dialog_box import DialogBox
from .ui_control import UIControl

class ListBox(UIControl):
    __selection: str = ""

    def __init__(self, owner: DialogBox) -> None:
        super().__init__(owner)

    def get_selection(self) -> str:
        return self.__selection

    def set_selection(self, selection: str):
        self.__selection = selection
        self._owner.changed(self)

    