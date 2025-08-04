
import time

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException, NoSuchElementException)


from ..settings import TIME_MAX, OS


class BasePage:
    def __init__(self, browser):
        self.__browser = browser

    def __define_os(self, field):
        if OS == "Windows" or OS == "Linux":
            self.__clean_win_uix(field)
        if OS == "Darwin":
            self.__clean_mac_os(field)

    def __clean_mac_os(self, field):
        "Для mac os"
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.DELETE)

    def __clean_win_uix(self, field):
        "Для windows и linux"
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)

    def clear_field(self, field):
        "Очистка поля"
        self.__define_os(field)

    def scrol_to_element(self, element):
        "Прокрутка страницы до элемента"
        self.__browser.execute_script("arguments[0].scrollIntoView();", element)

    def get_element(self, path):
        "Ожидание элемента"
        time_start = time.time()
        while True:
            try:
                element = self.__browser.find_element(*path)
                return element
            except NoSuchElementException as e:
                if time.time() - time_start > TIME_MAX:
                    raise e
                time.sleep(0.5)

    def get_button_click(self, path=None, element=None):
        "Ожидание нажатия"
        time_start = time.time()
        if element is None:
            button = self.get_element(path)
        else:
            button = element
        while True:
            try:
                button.click()
                return button
            except ElementClickInterceptedException as e:
                if time.time() - time_start > TIME_MAX:
                    raise e
                time.sleep(0.5)

    def open_url(self, url):
        "Открыть ссылку"
        self.__browser.get(url)

    def current_url(self):
        "Получение текущего url"
        return self.__browser.current_url

    def change_the_window(self, number_window):
        "Смена активного окна"
        new_window = self.__browser.window_handles[number_window]
        self.__browser.switch_to.window(new_window)

    def write_field(self, path, text):
        field = self.get_element(path)
        field.send_keys(text)

