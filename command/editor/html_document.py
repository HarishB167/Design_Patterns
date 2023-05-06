
class HtmlDocument:
    __content: str = ""

    def make_bold(self):
        self.__content = "<b>" + self.__content + "</b>"

    def get_content(self):
        return self.__content

    def set_content(self, content:str):
        self.__content = content

    
