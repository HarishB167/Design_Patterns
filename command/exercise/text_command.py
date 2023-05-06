from command.exercise.history import History
from command.exercise.video_editor import VideoEditor
from .undoable_command import UndoableCommandInterface

class TextCommand(UndoableCommandInterface):
    __text: str = ""
    __history: History = None
    __video_editor: VideoEditor = None

    def __init__(self, text:str, video_editor: VideoEditor, history: History):
        self.__text = text
        self.__video_editor = video_editor
        self.__history = history

    def execute(self):
        self.__video_editor.set_text(self.__text)
        self.__history.push(self)

    def unexecute(self):
        self.__video_editor.remove_text()
