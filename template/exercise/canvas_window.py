from .window import Window

class CanvasWindow(Window):

    def _before_window_close(self):
        print("Canvas : Work before window close")

    def _after_window_close(self):
        print("Canvas : Work after window close")