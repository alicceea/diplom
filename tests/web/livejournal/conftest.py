from time import sleep

import pytest
from selene import browser


from livejournal.utils.util import ConfigureLJ
from tests.util.config import add_screenshot, add_html, add_video, get_driver, is_local_run


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver = get_driver()
    browser.config.base_url = ConfigureLJ.base_person_url
    browser.config.timeout = 10.0

    yield

    add_screenshot(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def add_login():
    if not is_local_run():
        return

    browser.open(ConfigureLJ.login_url)
    browser.element('#user').type(ConfigureLJ.username)
    browser.element('#lj_loginwidget_password').type(ConfigureLJ.password) \
        .press_enter()
    sleep(ConfigureLJ.sleep_wait_medium)
