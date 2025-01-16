import os

import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

load_dotenv()


class Configure:
    is_local = os.getenv('is_local')
    selenoid_login = os.getenv('selenoid_login')
    selenoid_pass = os.getenv('selenoid_pass')
    selenoid_uri = os.getenv('selenoid_uri')
    selenoid_path = f'https://{selenoid_login}:{selenoid_pass}{selenoid_uri}'


def is_local_run():
    return Configure.is_local == 'true'


def get_driver():
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    # options.add_argument("--width=2560")
    # options.add_argument("--height=1440")
    options.timeouts = {'pageLoad': 10000}
    options.page_load_strategy = 'none'

    if is_local_run():
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
            command_executor=Configure.selenoid_path,
            options=options
        )
    return driver


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
