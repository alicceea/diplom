import pytest
from selene import browser

from sela.utils.util import ConfigureSela
from tests.util.config import add_screenshot, add_html, add_video, get_driver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver = get_driver()
    browser.config.base_url = ConfigureSela.base_url
    browser.config.timeout = 10

    yield

    add_screenshot(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()
