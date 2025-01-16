from time import sleep

import allure
from selene import Browser, have, query, be

from sela.utils.util import ConfigureSela

products_list = '//div[@id="products_list"]'
card = products_list + '/ul/li[{number}]'
favorite_button = card + '//button[contains(@class, "product-card__favorite")]'
add_to_cart_button = '//button[contains(@class, "product-card__title")]'


# document.evaluate('//*[@id="popmechanic-snippet"]//*[@data-popmechanic-close]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()

class PageSela:

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step("Пользователь открывает главную страницу")
    def open_main_page(self):
        self.browser.open('/')
        sleep(ConfigureSela.sleep_wait_medium)

    @allure.step("Пользователь выбирает предложенный город")
    def choose_recommended_city_modal(self):
        try:
            self.browser.element('//*[@class="js-choice-city-close-popup city-isset"]').click()
            sleep(ConfigureSela.sleep_wait_short)
        except Exception as e:
            print(e)

    @allure.step("Пользователь открывает вкладку 'Малыши'")
    def click_tab_baby(self):
        self.browser.element('//*[@data-tab="baby"]').click()
        sleep(ConfigureSela.sleep_wait_short)

    @allure.step("Пользователь открывает вкладку 'Мужчины'")
    def click_tab_men(self):
        self.browser.element('//*[@data-tab="men"]').click()
        sleep(ConfigureSela.sleep_wait_short)

    @allure.step("Пользователь открывает вкладку 'Женщины'")
    def click_tab_women(self):
        self.browser.element('//*[@data-tab="women"]').click()
        sleep(ConfigureSela.sleep_wait_short)

    @allure.step("Пользователь открывает вкладку 'Мальчики'")
    def click_tab_boys(self):
        self.browser.element('//*[@data-tab="boy"]').click()
        sleep(ConfigureSela.sleep_wait_short)

    @allure.step("Пользователь открывает вкладку 'Девочки'")
    def click_tab_girls(self):
        self.browser.element('//*[@data-tab="girl"]').click()
        sleep(ConfigureSela.sleep_wait_short)

    @allure.step("Пользователь нажимает на кнопку 'Смотреть всё'")
    def open_babies_clothes_page(self):
        self.browser.element('//*[@id="menu_tab-baby"]//a[text() = "Смотреть всё"]').click()
        sleep(ConfigureSela.sleep_wait_medium)

    @allure.step("Пользователь нажимает на кнопку 'Избранное'")
    def open_favorites(self):
        self.browser.element('#header_user_menu_favorite_link').click()
        sleep(ConfigureSela.sleep_wait_medium)

    #
    @allure.step("Пользователь закрывает модальное окно")
    def close_annoying_modal(self):
        try:
            self.browser.element('//*[@id="popmechanic-snippet"]//*[@data-popmechanic-close]').click()
        except Exception as e:
            print(e)


    def add_cloth_to_favorites(self, number):
        with allure.step("Пользователь добавляет товар в избранное"):
            self.browser.element(favorite_button.format(number=number)).click()
            sleep(ConfigureSela.sleep_wait_short)
            return self.browser.element(favorite_button.format(number=number)).get(query.attribute("data-product_id"))

    @allure.step("Проверка заголовка на странице Малыши")
    def assert_babies_clothes_page(self):
        self.browser.element('//h1[@data-title="Малыши"]').should(have.exact_text("ОДЕЖДА ДЛЯ МАЛЫШЕЙ"))

    @allure.step("Проверка заголовка на странице Избранное")
    def assert_favorites_page(self):
        self.browser.element('//h1[@data-title="Избранное"]').should(have.exact_text("ИЗБРАННОЕ"))

    def assert_cloth_bu_id_in_favorites(self, favorite_id):
        with allure.step("Проверка товара в избранном"):
            self.browser.element(products_list + f'//button[@data-product_id="{favorite_id}"]').should(be.existing)


    def add_cloth_to_cart(self, number):
        with allure.step("Пользователь добавляет товар в корзину"):
            self.browser.element(add_to_cart_button.format(number=number)).click()
            sleep(ConfigureSela.sleep_wait_short)
            return self.browser.element(add_to_cart_button.format(number=number)).get(query.attribute("data-product_id"))