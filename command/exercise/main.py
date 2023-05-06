from command.editor.undo_command import UndoCommand
from .video_editor import VideoEditor
from .history import History
from .text_command import TextCommand
from .contrast_command import ContrastCommand



if __name__ == "__main__":
    history = History()
    video_editor = VideoEditor()
    print(video_editor)
    video_editor.set_text("Hello World")
    TextCommand("Hello World", video_editor, history).execute()
    print(video_editor)
    ContrastCommand(5, video_editor, history).execute()

    print(video_editor)
    UndoCommand(history).execute()
    print(video_editor)
    UndoCommand(history).execute()
    print(video_editor)
