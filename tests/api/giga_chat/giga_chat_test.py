import json
from pathlib import Path

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
        response = requests.request("GET", ConfigureGigaChat.giga_chat_models_url, headers=headers, data={}, verify=False)
        body = response.json()

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    # todo napisat normalno
    with allure.step("Проверка json schema ответа"):
        with open(f"{Path(__file__).parent.parent.parent.parent}\\resource\\schemas\\models.json") as file:
            validate(body, schema=json.loads(file.read()))

    with allure.step("Проверка количества доступных моделей"):
        assert len(body['data']) == 4


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Отправка запроса в чат")
def test_giga_api_text_generate(headers):
    with allure.step("Отправка запроса на получение ответа от гигачат"):
        response = requests.request("POST", ConfigureGigaChat.giga_chat_text_url, headers=headers, data=text_data, verify=False)
        body = response.json()

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

    # todo napisat normalno
    with allure.step("Проверка json schema ответа"):
        with open(f"{Path(__file__).parent.parent.parent.parent}\\resource\\schemas\\chat.json") as file:
            validate(body, schema=json.loads(file.read()))

    with allure.step("Проверка роли отвечающего"):
        assert body['choices'][0]['message']['role'] == 'assistant'


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Diplom project')
@allure.title("Неавторизованный пользователь не может отправить запрос")
def test_giga_api_unauthorized():
    with allure.step("Отправка запроса неавторизованного пользователя"):
        response = requests.request("POST", ConfigureGigaChat.giga_chat_text_url, headers={}, data=text_data, verify=False)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 401

    with allure.step("Проверка тела ответа"):
        assert response.json() == {'message': 'Unauthorized', 'status': 401}
