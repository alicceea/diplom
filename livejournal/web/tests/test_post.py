import allure
from allure_commons.types import Severity
from selene import browser

from livejournal.web.data.test_objects import dog_post, cat_post
from livejournal.web.pages.pages import PagePost

page_post = PagePost(browser)
post_info_create = dog_post()
post_info_update = cat_post()

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.story("Пользователь создает: редактирует и удаляет пост")
@allure.title("Crud operations with post")
def test_post_page(add_login):
    create_post()
    update_post()
    delete_post()

@allure.step("Пользователь создает пост")
def create_post():
    page_post.open_profile()
    page_post.create_post(post_info_create)

    page_post.assert_post_page(post_info_create)

@allure.step("Пользователь редактирует пост")
def update_post():
    page_post.open_profile()
    page_post.assert_have_post(post_info_create)

    page_post.update_post(post_info_create.uuid, post_info_update)

    page_post.assert_post_page(post_info_update)

@allure.step("Пользователь удаляет пост")
def delete_post():
    page_post.open_profile()
    page_post.assert_have_not_post(post_info_create)
    page_post.assert_have_post(post_info_update)

    page_post.delete_post(post_info_update.uuid)

    page_post.assert_have_not_post(post_info_update)
