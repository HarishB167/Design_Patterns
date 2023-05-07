from .ui_control import UIControl

class Button(UIControl):
    __is_enabled: bool = False

    def is_enabled(self) -> bool:
        return self.__is_enabled

    def set_enabled(self, is_enabled: bool):
        self.__is_enabled = is_enabled
        self.notify_observers()

