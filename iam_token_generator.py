import os
import time
import json
import requests
import jwt  # pyjwt
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization

class IAMTokenManager:
    def __init__(self, sa_key_env_var="SA_KEY", token_ttl=3600):
        self.token_ttl = token_ttl  # Время жизни токена в секундах (~1 час)
        self.iam_token = None
        self.token_created_at = 0

        sa_key_json = os.getenv(sa_key_env_var)
        if not sa_key_json:
            raise ValueError(f"Переменная окружения {sa_key_env_var} не установлена")

        self.key_data = json.loads(sa_key_json)

        # Загружаем нужные поля из ключа
        self.service_account_id = self.key_data.get("id")
        self.private_key = self.key_data.get("private_key")
        if not self.service_account_id or not self.private_key:
            raise ValueError("В service account ключе нет 'id' или 'private_key'")

        # Парсим приватный ключ в объект для подписи
        self.private_key_obj = serialization.load_pem_private_key(
            self.private_key.encode("utf-8"),
            password=None
        )

    def create_jwt(self):
        now = int(time.time())

        # Стандартные заголовки JWT
        headers = {
            "alg": "PS256",
            "typ": "JWT"
        }

        # Поля payload JWT — стандарт для Yandex IAM
        payload = {
            "iss": self.service_account_id,           # issuer — service account id
            "aud": "https://iam.api.cloud.yandex.net/iam/v1/tokens",
            "iat": now,
            "exp": now + 3600                          # время жизни токена (1 час)
        }

        # Генерируем JWT с PS256 подписью (RSA PSS + SHA256)
        encoded_jwt = jwt.encode(
            payload,
            self.private_key_obj,
            algorithm="PS256",
            headers=headers
        )

        return encoded_jwt

    def get_iam_token(self):
        now = time.time()
        if not self.iam_token or now - self.token_created_at > self.token_ttl:
            jwt_token = self.create_jwt()

            url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
            headers = {"Content-Type": "application/json"}
            data = {
                "jwt": jwt_token
            }

            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                self.iam_token = response.json()["iamToken"]
                self.token_created_at = now
                print("🔄 IAM токен обновлён с помощью JWT")
            else:
                raise RuntimeError(f"Не удалось получить IAM токен: {response.status_code} {response.text}")

        return self.iam_token
