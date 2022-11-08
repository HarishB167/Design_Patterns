from .editor_state import EditorState

class Editor:
    __content = "";

    def createState(self):
        return EditorState(self.__content)

    def restore(self, state):
        self.__content = state.getContent()

    def getContent(self):
        return self.__content

    def setContent(self, content):
        self.__content = content

