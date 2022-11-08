from .tool_interface import ToolInterface

class EraserTool(ToolInterface):
    def mouseDown(self):
        print("Eraser icon")

    def mouseUp(self):
        print("Erase something")