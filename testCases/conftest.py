from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")