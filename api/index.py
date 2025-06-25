from fastapi import FastAPI, Request, status
from contextlib import asynccontextmanager
import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"),
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


# Обработчики
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот салона красоты.")


# Важно: создаем отдельную сессию для каждого запроса
async def with_bot_session(update_data: dict):
    async with bot.context() as ctx_bot:
        update = types.Update.model_validate(update_data)
        await dp.feed_update(ctx_bot, update)


@asynccontextmanager
async def lifespan(app: FastAPI):
    webhook_url = f"{os.getenv('WEBHOOK_URL')}/webhook"
    await bot.set_webhook(
        url=webhook_url,
        drop_pending_updates=True
    )
    yield
    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def webhook_handler(request: Request):
    try:
        # Проверка secret token


        # Создаем задачу с новой сессией
        update_data = await request.json()
        asyncio.create_task(with_bot_session(update_data))

        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return {"status": "error"}
