from typing import List
from .fx.command_interface import CommandInterface

class CompositeCommand(CommandInterface):
    __commands: List[CommandInterface] = []

    def add(self, command: CommandInterface):
        self.__commands.append(command)

    def execute(self):
        for command in self.__commands:
            command.execute()