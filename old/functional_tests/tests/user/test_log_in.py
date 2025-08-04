from functional_tests.pages.user_page import UserPage
from functional_tests.urls.urls import URLS
from functional_tests.data.form import UserForm
import time


class TestCaseUserLogIn:

    def test_login_user_correct_data(self, browser_def):
        data = UserForm.get_data("correct")
        page = UserPage(browser_def)
        page.open_url(URLS['/'])
        page.user_login(**data)
        assert page.current_url() == URLS["product-list"]

    def test_login_uncurrect_user_data(self, browser_def):
        data = UserForm.get_data("uncorrect")
        page = UserPage(browser_def)
        page.open_url(URLS['/'])
        page.user_login(**data)
        assert page.current_url() == URLS["log-in"]