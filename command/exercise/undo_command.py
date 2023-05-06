from .command_interface import CommandInterface
from .history import History

class UndoCommand(CommandInterface):
    __history: History = None

    def __init__(self, history: History):
        self.__history = history

    def execute(self):
        if self.__history.size() > 0:
            self.__history.pop().unexecute()