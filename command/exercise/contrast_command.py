from command.exercise.history import History
from command.exercise.video_editor import VideoEditor
from .undoable_command import UndoableCommandInterface

class ContrastCommand(UndoableCommandInterface):
    __contrast: str = ""
    __prev_contrast: str = ""
    __history: History = None
    __video_editor: VideoEditor = None

    def __init__(self, contrast:float, video_editor: VideoEditor, history: History):
        self.__contrast = contrast
        self.__video_editor = video_editor
        self.__history = history

    def execute(self):
        self.__prev_contrast = self.__video_editor.get_contrast()
        self.__video_editor.set_contrast(self.__contrast)
        self.__history.push(self)

    def unexecute(self):
        self.__video_editor.set_contrast(self.__prev_contrast)
