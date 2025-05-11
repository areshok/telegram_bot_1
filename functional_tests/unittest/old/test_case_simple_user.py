import os
import unittest
import time
import sqlite3


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import dotenv

import params

import pprint

dotenv.load_dotenv('test.env')


DEBUG_TRUE_STR = 'You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.'




class SimpleUserTest(unittest.TestCase):
    "Тестирование сайта обычный пользователь"

    @classmethod
    def setUpClass(cls):
        cls.user = {
            'username': os.getenv('TEST_USERNAME'),
            'password': os.getenv('TEST_PASSWORD')
        }
        cls.base_url = os.getenv('TEST_URL')

        # браузер
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-cache")  # Отключение кеша
        chrome_options.add_argument("--incognito")
        cls.browser = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        pass

    def tearDown(self):
        result = "УСПЕШНО" if self._outcome.success else "ПРОВАЛЕН"
        print(f'{self._testMethodName} - {self._outcome.result}')
        #pprint.pprint(self._outcome.result.errors)
        #print(f"Тест завершён: {self.id()} - {result} - {self._outcome.result}")

    def get_url(self, namespace):
        url = params.urls.get(namespace)
        if url is None:
            self.assertRaises()
        else:
            full_url = self.base_url + url
            return full_url


    def test_1_log_in(self):
        "Тест входа в систему обычного пользователя"
        self.browser.get(self.base_url)

        username = self.browser.find_element(By.ID, 'id_username')
        password = self.browser.find_element(By.ID, 'id_password')
        username.send_keys(os.getenv('TEST_USERNAME'))
        password.send_keys(os.getenv('TEST_PASSWORD'))
        login_buttom = self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_buttom.click()
        current_url = self.browser.current_url
        time.sleep(1)
        self.assertEqual(current_url, 'http://127.0.0.1:8000/product/')

    def test_2_create_product(self):
        "Тест создание товара обычным пользователем"

        url = self.get_url('product:product_create')
        self.browser.get(url)

        # id_name
        product_name = self.browser.find_element(By.ID, 'id_name')
        product_descriptions = self.browser.find_element(By.ID, 'id_description')

        product_name.send_keys('product_test_name')
        product_descriptions.send_keys('product_test_descriptions')

        form_button = self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        form_button.click()
        time.sleep(1)
        # не завершено

    def test_test(self):
        self.assertEqual(1,2)

    def test_33_product_list_content(self):
        pass

    def test_33_product_list_buttoms(self):
        pass

    def test_3_product_list_paginations(self):
        pass
    
    def test_4_feedback_get(self):
        pass

    def test_5_feedback_paginations(self):
        pass

    def test_6_username_in_header(self):
        pass

    def test_7_navbar_brand_url(self):
        pass

    def test_4_permmision_admin_zone(self):
        pass
        
    def test_999_user_logout(self):
        pass