from .fx.command_interface import CommandInterface

class BlackAndWhiteCommand(CommandInterface):
    def execute(self):
        print("Black and white")