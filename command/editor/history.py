from typing import List
from .undoable_command import UndoableCommandInterface


class History:
    __command: List[UndoableCommandInterface] = []

    def push(self, command: UndoableCommandInterface):
        self.__command.append(command)
    
    def pop(self) -> UndoableCommandInterface:
        return self.__command.pop()

    def size(self) -> int:
        return len(self.__command)