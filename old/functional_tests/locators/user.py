from selenium.webdriver.common.by import By

class UserLocator:
    class Create:
        pass

    class LogIn:
        username = (By.XPATH, ".//input[@id='id_username']")
        password = (By.XPATH, ".//input[@id='id_password']")
        enter = (By.XPATH, ".//button[text()='Войти']")