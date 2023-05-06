from .dialog_box import DialogBox


class UIControl:
    _owner: DialogBox = None
    
    def __init__(self, owner: DialogBox) -> None:
        self._owner = owner