import pytest
import requests

from giga_chat.util.util import ConfigureGigaChat, use_token


@pytest.fixture(scope='session', autouse=True)
def headers():
    return get_giga_token_headers()


def get_giga_token_headers():
    if use_token():
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {ConfigureGigaChat.giga_chat_token}'
        }

    payload = {
        'scope': 'GIGACHAT_API_PERS'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': '6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e',
        'Authorization': f'Basic {ConfigureGigaChat.giga_chat_auth}'
    }

    response = requests.request("POST", url=ConfigureGigaChat.giga_chat_auth_url, headers=headers, data=payload,
                                verify=False)
    token = response.json()['access_token']
    print("token: " + token)
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
