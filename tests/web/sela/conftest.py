
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from sela.utils.util import ConfigureSela
from tests.util.config import Configure, add_screenshot, add_html, add_video


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    is_run_locally = request.config.getoption('--run_local') == 'true'

    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    # options.add_argument("--width=2560")
    # options.add_argument("--height=1440")
    options.timeouts = {'pageLoad': 10000}
    options.page_load_strategy = 'none'

    if is_run_locally:
        driver = webdriver.Firefox(options=options)
    else:
        options.set_capability('browserName', 'firefox')
        options.set_capability('browserVersion', '125.0')
        options.page_load_strategy = 'eager'
        options.set_capability('selenoid:options', {
            'enableVNC': True,
            'enableVideo': True
        })

        driver = webdriver.Remote(
            command_executor=f'https://{Configure.selenoid_login}:{Configure.selenoid_pass}@selenoid.autotests.cloud/wd/hub',
            options=options
        )
    browser.config.driver = driver
    browser.config.base_url = ConfigureSela.base_url
    browser.config.timeout = 10

    yield

    if is_run_locally:
        add_screenshot(browser)
        add_html(browser)
        add_video(browser)

    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--run_local',
        action='store',
        default='true'
    )