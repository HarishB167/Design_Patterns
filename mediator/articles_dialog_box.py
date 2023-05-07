from .observer import Observer
from .ui_control import UIControl
from .list_box import ListBox
from .text_box import TextBox
from .button import Button

class ArticlesDialogBox:
    __articles_list_box: ListBox = None
    __title_text_box: TextBox = None
    __save_button: Button = None

    def __init__(self) -> None:
        self.__articles_list_box = ListBox()
        self.__articles_list_box.attach(type('NewObserver', (object,), dict(update=self.__article_selected)))
        self.__title_text_box = TextBox()
        self.__title_text_box.attach(type('NewObserver', (object,), dict(update=self.__title_changed)))
        self.__save_button = Button()

    def simulate_user_interaction(self):
        self.__articles_list_box.set_selection("Article 1")
        self.__title_text_box.set_content("")
        self.__title_text_box.set_content("Article 2")
        print("Textbox : " + self.__title_text_box.get_content())
        print("Button : " + str(self.__save_button.is_enabled()))

    def __title_changed(self):
        content = self.__title_text_box.get_content()
        isEmpty = content == None or len(content) == 0
        self.__save_button.set_enabled(not isEmpty)

    def __article_selected(self):
        self.__title_text_box\
            .set_content(self.__articles_list_box.get_selection())
        self.__save_button.set_enabled(True)
