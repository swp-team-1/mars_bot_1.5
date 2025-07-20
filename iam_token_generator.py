import os
import time
import json
from yandexcloud import SDK

class IAMTokenManager:
    def __init__(self, token_ttl=3600):
        self.token_ttl = token_ttl  # 1 час
        self.iam_token = None
        self.token_created_at = 0
        
        # Получаем ключ сервисного аккаунта из переменных окружения
        sa_key_json = os.getenv("SA_KEY")
        if not sa_key_json:
            raise ValueError("Переменная SA_KEY не установлена")
        
        try:
            # Парсим JSON из переменной окружения
            sa_key = json.loads(sa_key_json)
            self.sdk = SDK(service_account_key=sa_key)
        except json.JSONDecodeError:
            raise ValueError("Неверный формат JSON в SA_KEY")
        except Exception as e:
            raise ValueError(f"Ошибка инициализации SDK: {str(e)}")

    def get_iam_token(self):
        now = time.time()
        if not self.iam_token or now - self.token_created_at > self.token_ttl:
            try:
                # Получаем IAM токен через SDK
                iam_token = self.sdk._client_credentials.iam_token
                if not iam_token:
                    raise ValueError("Не удалось получить IAM токен")
                
                self.iam_token = iam_token
                self.token_created_at = now
                print("🔄 IAM токен успешно обновлен")
            except Exception as e:
                print(f"❌ Ошибка при получении IAM токена: {str(e)}")
                raise
        return self.iam_token

# Инициализация
try:
    iam_manager = IAMTokenManager()
    IAM_TOKEN = iam_manager.get_iam_token()
    print(f"✅ IAM токен получен: {IAM_TOKEN[:10]}...")  # Логируем только начало токена
except Exception as e:
    print(f"❌ Критическая ошибка: {str(e)}")
    IAM_TOKEN = None
    # Здесь можно добавить дополнительные действия при ошибке
