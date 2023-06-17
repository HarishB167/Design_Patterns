from ..button import Button
from ..textbox import TextBox
from ..widget_factory import WidgetFactory
from .ant_button import AntButton
from .ant_textbox import AntTextBox

class AntWidgetFactory(WidgetFactory):

    def create_button(self) -> Button:
        return AntButton()

    def create_textbox(self) -> TextBox:
        return AntTextBox()
