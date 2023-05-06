from .command_interface import CommandInterface

class UndoableCommandInterface(CommandInterface):
    def unexecute(self):
        pass