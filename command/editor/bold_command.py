from .undoable_command import UndoableCommandInterface
from .html_document import HtmlDocument
from .history import History

class BoldCommand(UndoableCommandInterface):
    __prev_content: str = ""
    __document: HtmlDocument = None
    __history: History = None
    
    def __init__(self, document: HtmlDocument, history: History):
        self.__document = document
        self.__history = history

    def execute(self):
        self.__prev_content = self.__document.get_content()
        self.__document.make_bold()
        self.__history.push(self)

    def unexecute(self):
        self.__document.set_content(self.__prev_content)
        