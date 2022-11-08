from abc import ABC, abstractmethod

class Window(ABC):

    def close(self):
        self._before_window_close()
        print("Removing the window from the screen")
        self._after_window_close()

    @abstractmethod
    def _before_window_close(self):
        pass

    @abstractmethod
    def _after_window_close(self):
        pass
