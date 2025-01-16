import allure
from allure_commons.types import Severity
from selene import browser

from livejournal.data.test_objects import dog_post, cat_post
from livejournal.pages.pages import PagePost

page_post = PagePost(browser)
post_info_create = dog_post()
post_info_update = cat_post()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь создает пост")
def test_create_post(add_login):
    page_post.open_profile()
    page_post.create_post(post_info_create)

    page_post.assert_post_page(post_info_create)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь редактирует пост")
def test_update_post(add_login):
    page_post.open_profile()
    page_post.assert_have_post(post_info_create)

    page_post.update_post(post_info_create.uuid, post_info_update)

    page_post.assert_post_page(post_info_update)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь удаляет пост")
def test_delete_post(add_login):
    page_post.open_profile()
    page_post.assert_have_not_post(post_info_create)
    page_post.assert_have_post(post_info_update)

    page_post.delete_post(post_info_update.uuid)

    page_post.assert_have_not_post(post_info_update)
