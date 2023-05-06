from .command_interface import CommandInterface

class Button:
    __label = ""
    __command :CommandInterface = None

    def __init__(self, command: CommandInterface):
        self.__command = command

    def click(self):
        self.__command.execute()

    def getLabel(self):
        return self.__label

    def setLabel(self, label):
        self.__label = label
