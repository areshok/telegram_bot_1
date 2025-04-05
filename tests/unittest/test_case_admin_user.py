import unittest


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys





class AdminTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-cache")  # Отключение кеша
        chrome_options.add_argument("--incognito")
        cls.browser = webdriver.Chrome(options=chrome_options)

