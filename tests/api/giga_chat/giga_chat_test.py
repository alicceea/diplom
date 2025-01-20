import importlib.resources
import json

import allure
import requests
from allure_commons.types import Severity
from jsonschema import validate

from giga_chat.data.test_objects import text_data
from giga_chat.util.util import ConfigureGigaChat


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Получение доступных моделей")
def test_giga_api_models(headers):
    with allure.step("Отправка запроса на получение доступных моделей"):
        response = requests.request("GET", ConfigureGigaChat.giga_chat_models_url, headers=headers, data={},
                                    verify=False)

    assert_status_code(response, 200)
    assert_response_body_schema(response.json(), "models.json")

    with allure.step("Проверка количества доступных моделей"):
        assert len(response.json()['data']) == 4


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Отправка запроса в чат")
def test_giga_api_text_generate(headers):
    with allure.step("Отправка запроса на получение ответа от гигачат"):
        response = requests.request("POST", ConfigureGigaChat.giga_chat_text_url, headers=headers, data=text_data,
                                    verify=False)
    assert_status_code(response, 200)
    assert_response_body_schema(response.json(), "chat.json")

    with allure.step("Проверка роли отвечающего"):
        assert response.json()['choices'][0]['message']['role'] == 'assistant'


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Неавторизованный пользователь не может отправить запрос")
def test_giga_api_unauthorized():
    with allure.step("Отправка запроса неавторизованного пользователя"):
        response = requests.request("POST", ConfigureGigaChat.giga_chat_text_url, headers={}, data=text_data,
                                    verify=False)

    assert_status_code(response, 401)

    with allure.step("Проверка тела ответа"):
        assert response.json() == {'message': 'Unauthorized', 'status': 401}


def assert_status_code(response, expected_status_code):
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == expected_status_code


def assert_response_body_schema(body, schema_name):
    with allure.step("Проверка json schema ответа"):
        with importlib.resources.path("resources.schemas", schema_name) as template_file:
            with template_file.open() as file:
                validate(body, schema=json.loads(file.read()))
