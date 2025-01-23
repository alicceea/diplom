import allure
import pytest
from allure_commons.types import Severity
from selene import browser

from livejournal.data.post_data_objects import dog_post, cat_post
from livejournal.pages.pages import PagePost
from tests.util.config import is_local_run

page_post = PagePost(browser)
post_info_create = dog_post()
post_info_update = cat_post()


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь создает пост")
@pytest.mark.skipif(not is_local_run(), reason="Удаленно не работает :(")
def test_create_post(add_login):
    page_post.open_profile()
    page_post.create_post(post_info_create)

    page_post.assert_post_page(post_info_create)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Пользователь редактирует пост")
@pytest.mark.skipif(not is_local_run(), reason="Удаленно не работает :(")
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
@pytest.mark.skipif(not is_local_run(), reason="Удаленно не работает :(")
def test_delete_post(add_login):
    page_post.open_profile()
    page_post.assert_have_not_post(post_info_create)
    page_post.assert_have_post(post_info_update)

    page_post.delete_post(post_info_update.uuid)

    page_post.assert_have_not_post(post_info_update)
