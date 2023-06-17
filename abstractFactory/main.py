from .app.contact_form import ContactForm
from .material.material_widget_factory import MaterialWidgetFactory
from .ant.ant_widget_factory import AntWidgetFactory

if __name__ == "__main__":
    ContactForm().render(AntWidgetFactory())
