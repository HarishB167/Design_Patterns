from .ui_control import UIControl

class Button(UIControl):
    def __init__(self):
        super().__init__()
        self.__is_enabled: bool = False

    def is_enabled(self) -> bool:
        return self.__is_enabled

    def set_enabled(self, enabled: bool) -> None:
        self.__is_enabled = enabled
        self.notify_observers()
