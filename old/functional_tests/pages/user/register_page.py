from ..base import BasePage




class RegisterPage(BasePage):
    
    def write_username(self, text):
        self.write_field(self.get_element(path=''), text)

    def write_password(self, text):
        self.write_field(self.get_element(path=''), text)

    def click_button_form(self):
        self.get_button_click(path='')

    def completed_form(self, username, password):
        self.write_username(username)
        self.write_password(password)
        self.click_button_form()