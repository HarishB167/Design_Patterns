from .ui_control import UIControl

class CheckBox(UIControl):
    def __init__(self):
        super().__init__()
        self.__is_checked: bool = False

    def is_checked(self) -> bool:
        return self.__is_checked

    def set_checked(self, checked: bool) -> None:
        self.__is_checked = checked
        self.notify_observers()
