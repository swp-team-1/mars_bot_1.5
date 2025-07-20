import os
import time
import json
from yandexcloud import SDK

class IAMTokenManager:
    def __init__(self, sa_key_env_var: str = "SA_KEY", token_ttl=3600):
        self.token_ttl = token_ttl  # Время жизни токена в секундах
        self.iam_token = None
        self.token_created_at = 0

        sa_key_json = os.getenv(sa_key_env_var)
        if not sa_key_json:
            raise ValueError(f"Ошибка: переменная окружения {sa_key_env_var} не установлена")

        # Парсим JSON из переменной окружения
        key_data = json.loads(sa_key_json)
        self.sdk = SDK(service_account_key=key_data)

    def get_iam_token(self):
        now = time.time()
        if not self.iam_token or now - self.token_created_at > self.token_ttl:
            credentials = self.sdk.get_credentials()
            self.iam_token = credentials.iam_token
            self.token_created_at = now
            print("🔄 IAM токен обновлён")
        return self.iam_token


# Пример использования
iam_manager = IAMTokenManager()

# Получаем актуальный IAM токен
IAM_TOKEN = iam_manager.get_iam_token()
