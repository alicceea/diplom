from time import sleep

from selene import be, have, Browser
from selenium.webdriver import Keys

from livejournal.utils.util import ConfigureLJ


# document.evaluate('//*[@data-rd-type="rd-post-actions-popup"]/div/button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()

class PageHandler:
    browser: Browser

    def __init__(self, browser):
        self.browser = browser

    def open_profile(self):
        self.browser.open('/')
        sleep(ConfigureLJ.sleep_wait_medium)


class PagePost(PageHandler):
    def create_post(self, post):
        self.open_post_creation()
        self.close_draft_modal()
        self.fill_post(post)
        self.make_save_post()

    def update_post(self, old_uuid, post):
        self.open_post_by_uuid(old_uuid)
        self.edit_post()
        self.close_draft_modal()
        self.clear_post()
        self.fill_post(post)
        self.make_update_post()

    def delete_post(self, uuid):
        self.open_post_by_uuid(uuid)
        self.edit_post()
        self.close_draft_modal()
        self.make_delete_post()

    def assert_post_page(self, post):
        self.browser.element('//*[@class="aentry-post__title-text"]').should(have.exact_text(post.title))
        self.browser.element('//*[@class="aentry-post__content"]').should(have.text(post.uuid))

    def assert_have_post(self, post):
        self.browser.element(f'//a[text() = "{post.title}"]').should(be.existing)

    def assert_have_not_post(self, post):
        self.browser.element(f'//a[text() = "{post.title}"]').should(be.not_.existing)

    def make_save_post(self):
        self.browser.element('//span[text() = "Настроить и опубликовать"]').click()
        self.browser.element('//span[text() = "Опубликовать"]').click()
        sleep(ConfigureLJ.sleep_wait_medium)

    def make_update_post(self):
        self.browser.element('//span[text() = "Настроить и обновить"]').click()
        self.browser.element('//span[text() = "Обновить"]').click()
        sleep(ConfigureLJ.sleep_wait_medium)

    def make_delete_post(self):
        self.browser.element('//a[text() ="Удалить пост"]').click()
        self.browser.element('//span[text() = "Удалить"]').click()
        sleep(ConfigureLJ.sleep_wait_medium)

    def fill_post(self, post):
        self.browser.element('//*[@placeholder="Придумайте заголовок"]').type(post.title)
        self.browser.element('//div[@class="notranslate public-DraftEditor-content"]') \
            .send_keys(post.content)

    def clear_post(self):
        self.browser.element('//*[@placeholder="Придумайте заголовок"]').set_value('')
        self.browser.element('//div[@class="notranslate public-DraftEditor-content"]') \
            .send_keys(Keys.CONTROL + "a") \
            .send_keys(Keys.BACKSPACE)

    def open_post_creation(self):
        self.browser.element('//*[@class="s-header-item-post--long"]/parent::*').click()
        sleep(ConfigureLJ.sleep_wait_short)

    def open_post_by_uuid(self, uuid):
        self.browser.element(f'//a[text()[contains(.,"{uuid}")]]').click()
        sleep(ConfigureLJ.sleep_wait_short)

    def edit_post(self):
        self.browser.element('//*[@data-rd-type="rd-post-actions-popup"]/div/button').click()
        self.browser.element('//span[text() = "Редактировать запись"]').click()

    def close_draft_modal(self):
        try:
            self.browser.element('//span[text() = "Нет, спасибо"]').click()
        except Exception as e:
            print("Попытка закрытия модального окна завершилась с ошибкой", e)
