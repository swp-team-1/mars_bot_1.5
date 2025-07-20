import os
import time
import json
import requests

class IAMTokenManager:
    def __init__(self, sa_key_env_var="SA_KEY", token_ttl=3600):
        self.token_ttl = token_ttl  # Время жизни токена в секундах (~1 час)
        self.iam_token = None
        self.token_created_at = 0

        sa_key_json = os.getenv(sa_key_env_var)
        if not sa_key_json:
            raise ValueError(f"Переменная окружения {sa_key_env_var} не установлена")

        self.key_data = json.loads(sa_key_json)

    def get_iam_token(self):
        now = time.time()
        if not self.iam_token or now - self.token_created_at > self.token_ttl:
            # Формируем тело запроса
            url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
            headers = {"Content-Type": "application/json"}

            # Для получения токена используем JWT из service account ключа
            # Но проще - если у вас есть уже OAuth токен в ключе, можно использовать его:
            if "oauth_token" in self.key_data:
                data = {
                    "yandexPassportOauthToken": self.key_data["oauth_token"]
                }
            else:
                # Если OAuth токена нет - используем service account id и private_key
                # Тогда нужно генерировать JWT (сложнее)
                # Пока поднимем ошибку
                raise RuntimeError("В service account ключе нет поля 'oauth_token', нужен OAuth токен для получения IAM токена вручную.")

            response = requests.post(url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                self.iam_token = response.json()["iamToken"]
                self.token_created_at = now
                print("🔄 IAM токен обновлён вручную")
            else:
                raise RuntimeError(f"Не удалось получить IAM токен: {response.status_code} {response.text}")

        return self.iam_token

# Инициализация менеджера токенов
iam_manager = IAMTokenManager()

# Пример функции для распознавания речи через SpeechKit
def speechkit_stt(voice_data, folder_id, lang="ru-RU"):
    iam_token = iam_manager.get_iam_token()
    headers = {
        "Authorization": f"Bearer {iam_token}",
        "Content-Type": "audio/ogg"
    }

    response = requests.post(
        "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize",
        headers=headers,
        params={"folderId": folder_id, "lang": lang},
        data=voice_data
    )

    if response.status_code == 200:
        return response.json().get("result")
    else:
        print(f"Ошибка STT: {response.status_code} {response.text}")
        return None
