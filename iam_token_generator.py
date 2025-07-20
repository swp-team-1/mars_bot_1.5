import time
import json
from yandexcloud import SDK

class IAMTokenManager:
    def __init__(self, key_path: str, token_ttl=3600):
        self.key_path = key_path
        self.token_ttl = token_ttl  # Время жизни токена в секундах
        self.iam_token = None
        self.token_created_at = 0

        with open(self.key_path, "r") as f:
            key_data = json.load(f)
            self.sdk = SDK(service_account_key=key_data)

    def get_iam_token(self):
        now = time.time()
        # Если токен отсутствует или просрочен, обновляем
        if not self.iam_token or now - self.token_created_at > self.token_ttl:
            credentials = self.sdk.get_credentials()
            self.iam_token = credentials.iam_token
            self.token_created_at = now
            print("🔄 IAM токен обновлён")
        return self.iam_token

# Пример использования:
iam_manager = IAMTokenManager("key.json")

# В нужный момент получить актуальный IAM токен:
IAM_TOKEN = iam_manager.get_iam_token()
