from time import sleep

import pytest
from selene import browser
from selenium.webdriver import FirefoxOptions

from livejournal.utils.util import Configure


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'firefox'
    browser.config.base_url = Configure.base_person_url
    browser.config.timeout = 3.0
    options = FirefoxOptions()
    options.add_argument("--width=2560")
    options.add_argument("--height=1440")
    # options.add_argument("--width=1920")
    # options.add_argument("--height=1080")
    options.timeouts = {'pageLoad': 3000}
    options.page_load_strategy = 'none'
    browser.config.driver_options = options

    yield

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def add_login():
    browser.open(Configure.login_url)
    browser.element('#user').type(Configure.username)
    browser.element('#lj_loginwidget_password').type(Configure.password) \
        .press_enter()
    sleep(Configure.sleep_wait_medium)
