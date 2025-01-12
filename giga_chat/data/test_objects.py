import json

text_data = json.dumps({
    "model": "GigaChat",
    "messages": [
        {
            "role": "system",
            "content": "Ты профессиональный переводчик на английский язык. Переведи точно сообщение пользователя."
        },
        {
            "role": "user",
            "content": "GigaChat — это сервис, который умеет взаимодействовать с пользователем в формате диалога, писать код, создавать тексты и картинки по запросу пользователя."
        }
    ],
    "stream": False,
    "update_interval": 0
})
