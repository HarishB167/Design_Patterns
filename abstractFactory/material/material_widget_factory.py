from ..button import Button
from ..textbox import TextBox
from ..widget_factory import WidgetFactory
from .material_button import MaterialButton
from .material_textbox import MaterialTextBox

class MaterialWidgetFactory(WidgetFactory):

    def create_button(self) -> Button:
        return MaterialButton()

    def create_textbox(self) -> TextBox:
        return MaterialTextBox()
