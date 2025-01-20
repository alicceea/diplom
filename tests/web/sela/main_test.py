import allure
from allure_commons.types import Severity
from selene import browser

from sela.pages.pages import PageSela

page_sela = PageSela(browser)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь просматривает все вкладки")
def test_open_all_tabs():
    page_sela.open_main_page()
    page_sela.choose_recommended_city_modal()

    page_sela.click_tab_men()
    page_sela.click_tab_women()
    page_sela.click_tab_boys()
    page_sela.click_tab_girls()
    page_sela.click_tab_baby()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь открывает вкладку 'Малыши' все товары")
def test_open_babies_clothes():
    page_sela.open_main_page()
    page_sela.choose_recommended_city_modal()

    page_sela.click_tab_baby()
    page_sela.open_babies_clothes_page()

    page_sela.assert_babies_clothes_page()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь открывает вкладку страницу 'Избранное'")
def test_open_favorites():
    page_sela.open_main_page()
    page_sela.choose_recommended_city_modal()
    page_sela.open_favorites()

    page_sela.assert_favorites_page()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь добавляет 3 первых товара в избранное")
def test_add_any_cloth_to_favorites():
    favorites_ids = []
    page_sela.open_main_page()
    page_sela.choose_recommended_city_modal()

    page_sela.click_tab_baby()
    page_sela.open_babies_clothes_page()

    page_sela.assert_babies_clothes_page()

    for i in range(1, 4):
        favorites_ids.append(
            page_sela.add_cloth_to_favorites(i)
        )

    page_sela.open_favorites()
    page_sela.assert_favorites_page()

    for favorite_id in favorites_ids:
        page_sela.assert_cloth_in_favorites(favorite_id)

    print(favorites_ids)
