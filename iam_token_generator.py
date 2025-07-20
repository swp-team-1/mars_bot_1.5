import os
import json
import time
import jwt  # pip install PyJWT
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Пути и переменные
KEY_PATH = "key.json"
FOLDER_ID = "b1gjscnkju98tsil5anj"

def get_iam_token_from_sa_key(json_key_path: str) -> str:
    """Генерация IAM токена из ключа сервисного аккаунта (SA Key)"""
    try:
        with open(json_key_path, "r") as f:
            sa_key = json.load(f)

        now = int(time.time())
        payload = {
            "aud": "https://iam.api.cloud.yandex.net/iam/v1/tokens",
            "iss": sa_key["service_account_id"],
            "iat": now,
            "exp": now + 360  # токен живёт 6 минут
        }

        jwt_token = jwt.encode(
            payload,
            sa_key["private_key"],
            algorithm="PS256",
            headers={"kid": sa_key["id"]}
        )

        response = requests.post(
            "https://iam.api.cloud.yandex.net/iam/v1/tokens",
            json={"jwt": jwt_token}
        )
        response.raise_for_status()
        return response.json()["iamToken"]

    except Exception as e:
        print(f"❌ Ошибка получения IAM токена: {e}")
        return None
