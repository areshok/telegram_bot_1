import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser_def():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def browser_admin():
    pass

@pytest.fixture()
def browser_auth_user():
    pass

@pytest.fixture()
def browser_anonim_user():
    pass

