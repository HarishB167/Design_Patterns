from .tool_interface import ToolInterface

class SelectionTool(ToolInterface):

    def mouseDown(self):
        print("Selection icon")

    def mouseUp(self):
        print("Draw a dashed rectangle")