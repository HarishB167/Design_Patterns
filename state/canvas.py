from .tool_interface import ToolInterface

class Canvas:

    __current_tool: ToolInterface = None
    
    def mouseDown(self):
        self.__current_tool.mouseDown()

    def mouseUp(self):
        self.__current_tool.mouseUp()

    def getCurrentTool(self):
        return self.__current_tool

    def setCurrentTool(self, current_tool):
        self.__current_tool = current_tool
