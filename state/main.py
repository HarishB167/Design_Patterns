from .canvas import Canvas
from .selection_tool import SelectionTool
from .brush_tool import BrushTool
from .eraser_tool import EraserTool

if __name__ == "__main__":
    canvas = Canvas()
    canvas.setCurrentTool(EraserTool())
    canvas.mouseDown()
    canvas.mouseUp()
