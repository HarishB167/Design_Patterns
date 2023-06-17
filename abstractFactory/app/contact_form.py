from ..widget_factory import WidgetFactory

class ContactForm:

    def render(self, factory: WidgetFactory):
        factory.create_textbox().render()
        factory.create_button().render()
        