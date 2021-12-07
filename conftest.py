import pytest
from time import sleep

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, required=True,
                     help="Select language for web page")


@pytest.fixture
def language(request):
    return request.config.getoption('--language')


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser

    sleep(10)
    browser.quit()
