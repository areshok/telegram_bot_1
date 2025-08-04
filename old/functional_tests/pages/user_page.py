from .base import BasePage
from ..locators.user import UserLocator



class UserPage(BasePage):

    def write_username(self, path, text):
        field = self.get_element(path)
        field.send_keys(text)

    def write_password(self, path, text):
        field = self.get_element(path)
        field.send_keys(text)

    def user_login(self, username, password):
        self.write_username(UserLocator.LogIn.username, username)
        self.write_password(UserLocator.LogIn.password, password)
        self.get_button_click(path=UserLocator.LogIn.enter)



    def user_registration(self, username, password):
        self.write_field(path=*UserLocator.)













