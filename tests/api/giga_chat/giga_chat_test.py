import json
from pathlib import Path

import requests
from jsonschema import validate

from giga_chat.data.test_objects import text_data
from giga_chat.util.util import ConfigureGigaChat


def test_giga_api_models(headers):
    response = requests.request("GET", ConfigureGigaChat.giga_chat_models_url, headers=headers, data={}, verify=False)
    body = response.json()

    assert response.status_code == 200
    # todo napisat normalno
    with open(f"{Path(__file__).parent.parent.parent.parent}\\resource\\schemas\\models.json") as file:
        validate(body, schema=json.loads(file.read()))

    assert len(body['data']) == 4


def test_giga_api_text_generate(headers):
    response = requests.request("POST", ConfigureGigaChat.giga_chat_text_url, headers=headers, data=text_data,
                                verify=False)
    body = response.json()

    assert response.status_code == 200

    # todo napisat normalno
    with open(f"{Path(__file__).parent.parent.parent.parent}\\resource\\schemas\\chat.json") as file:
        validate(body, schema=json.loads(file.read()))

    assert body['choices'][0]['message']['role'] == 'assistant'
