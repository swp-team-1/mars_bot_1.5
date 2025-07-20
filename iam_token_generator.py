import os
import time
import json
import requests
import yandexcloud 
print("Yandex Cloud SDK version:", yandexcloud.__version__)

class IAMTokenManager:
    def __init__(self, sa_key_env_var="SA_KEY", token_ttl=3600):
        self.token_ttl = token_ttl  # Время жизни токена в секундах (~1 час)
        self.iam_token = None
        self.token_created_at = 0

        sa_key_json = os.getenv(sa_key_env_var)
        if not sa_key_json:
            raise ValueError(f"Переменная окружения {sa_key_env_var} не установлена")

        key_data = json.loads(sa_key_json)
        self.sdk = SDK(service_account_key=key_data)

    def get_iam_token(self):
        now = time.time()
        if not self.iam_token or now - self.token_created_at > self.token_ttl:
            self.iam_token = self.sdk.service_account().get_iam_token().iam_token
            self.token_created_at = now
            print("🔄 IAM токен обновлён")
        return self.iam_token

# Инициализация менеджера токенов
iam_manager = IAMTokenManager()

# Используем функцию для получения актуального токена в вашем коде распознавания:
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
