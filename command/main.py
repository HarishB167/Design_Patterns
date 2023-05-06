from .editor.undo_command import UndoCommand
from .editor.bold_command import BoldCommand
from .editor.html_document import HtmlDocument
from .composite_command import CompositeCommand
from .add_customer_command import AddCustomerCommand
from .resize_command import ResizeCommand
from .black_and_white_command import BlackAndWhiteCommand
from .customer_service import CustomerService
from .fx.button import Button
from .editor.history import History

if __name__ == "__main__":
    # service = CustomerService()
    # command = AddCustomerCommand(service)
    # button = Button(command)
    # button.click()

    # Composite command
    # composite = CompositeCommand()
    # composite.add(ResizeCommand())
    # composite.add(BlackAndWhiteCommand())
    # composite.execute()

    history = History()
    document = HtmlDocument()
    document.set_content("Hello World")

    bold_command = BoldCommand(document, history)
    bold_command.execute()
    print(document.get_content())

    undo_command = UndoCommand(history)
    undo_command.execute()
    print(document.get_content())
