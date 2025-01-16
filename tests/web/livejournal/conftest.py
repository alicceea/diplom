from time import sleep

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from livejournal.utils.util import ConfigureLJ
from tests.util.config import add_screenshot, add_html, add_video


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    # options.add_argument("--width=2560")
    # options.add_argument("--height=1440")
    options.timeouts = {'pageLoad': 10000}
    options.page_load_strategy = 'none'

    browser.config.driver = webdriver.Firefox(options=options)
    browser.config.base_url = ConfigureLJ.base_person_url
    browser.config.timeout = 10.0

    yield

    add_screenshot(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def add_login():
    browser.open(ConfigureLJ.login_url)
    browser.element('#user').type(ConfigureLJ.username)
    browser.element('#lj_loginwidget_password').type(ConfigureLJ.password) \
        .press_enter()
    sleep(ConfigureLJ.sleep_wait_medium)
