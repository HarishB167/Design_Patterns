
from .document_state import DocumentState


class Document:

    __content = ""
    __font_name = ""
    __font_size = 0

    def getContent(self):
        return self.__content

    def setContent(self, content):
        self.__content = content

    def getFontName(self):
        return self.__font_name

    def setFontName(self, font_name):
        self.__font_name = font_name

    def getFontSize(self):
        return self.__font_size

    def setFontSize(self, font_size):
        self.__font_size = font_size
   

    def createState(self):
        state = {
            "content": self.__content,
            "font_name": self.__font_name,
            "font_size": self.__font_size
        }
        return DocumentState(state)

    def restore(self, state: DocumentState):
        state = state.getState()
        self.__content = state["content"]
        self.__font_name = state["font_name"]
        self.__font_size = state["font_size"]

        
    def __str__(self):
        return ("Document{"
                "content='" + self.__content + '\'' +
                ", fontName='" + self.__font_name + '\'' +
                ", fontSize=" + str(self.__font_size) +
                '}')