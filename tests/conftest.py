from selene import browser
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options.add_argument(('--headless'))
