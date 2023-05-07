from .ui_control import UIControl
from .text_box import TextBox
from .button import Button
from .check_box import CheckBox

class SignupDialogBox:

    def __init__(self) -> None:
        self.__username_input = TextBox()
        self.__password_input = TextBox()
        self.__terms_input = CheckBox()
        self.__signup_button = Button()
        self.__username_input.attach(type('NewObserver', (object,), dict(update=self.__username_changed)))
        self.__password_input.attach(type('NewObserver', (object,), dict(update=self.__password_changed)))
        self.__terms_input.attach(type('NewObserver', (object,), dict(update=self.__terms_toggled)))

    def simulate_user_interaction(self):
        self.__username_input.set_content("John")
        print(self)
        self.__password_input.set_content("new pass")
        print(self)
        self.__terms_input.set_checked(True)
        # print("Username : " + self.__username_input.get_content())
        # print("Password : " + self.__password_input.get_content())
        # print("Terms checked : " + str(self.__terms_input.is_checked()))
        # print("Button : " + str(self.__signup_button.is_enabled()))
        print(self)
        self.__password_input.set_content("")
        # print("Button : " + str(self.__signup_button.is_enabled()))
        print(self)

    def __username_changed(self):
        self.__signup_button_check_n_enable()

    def __password_changed(self):
        self.__signup_button_check_n_enable()

    def __terms_toggled(self):
        self.__signup_button_check_n_enable()

    def __signup_button_check_n_enable(self):
        username = self.__username_input.get_content()
        usernameIsEmpty = username == None or len(username) == 0
        password = self.__password_input.get_content()
        passwordIsEmpty = password == None or len(password) == 0
        termsIsChecked = self.__terms_input.is_checked()
        self.__signup_button.set_enabled(not (usernameIsEmpty or passwordIsEmpty) and termsIsChecked)

    def __str__(self) -> str:
        username = self.__username_input.get_content()
        password = self.__password_input.get_content()
        terms = str(self.__terms_input.is_checked())
        button = str(self.__signup_button.is_enabled())
        text = f"SignupDialogBox(username='{username}', password='{password}', terms='{terms}', signupBtn='{button}')"
        return text

