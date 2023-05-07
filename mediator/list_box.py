from .ui_control import UIControl

class ListBox(UIControl):
    __selection: str = ""

    def get_selection(self) -> str:
        return self.__selection

    def set_selection(self, selection: str):
        self.__selection = selection
        self.notify_observers()

    