import os

from dotenv import load_dotenv

load_dotenv()


class ConfigureGigaChat:
    giga_chat_auth = os.getenv('giga_chat_auth')
    giga_chat_token = os.getenv('giga_chat_token')
    giga_chat_auth_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    giga_chat_models_url = "https://gigachat.devices.sberbank.ru/api/v1/models"
    giga_chat_text_url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

