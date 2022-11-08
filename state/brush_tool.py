from .tool_interface import ToolInterface

class BrushTool(ToolInterface):

    def mouseDown(self):
        print("Brush icon")

    def mouseUp(self):
        print("Draw a line")