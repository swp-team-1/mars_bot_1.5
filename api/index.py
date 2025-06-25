from fastapi import FastAPI, Request, status
from contextlib import asynccontextmanager
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получение переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_PATH = "/webhook"


# Инициализация бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


def get_about_us_text() -> str:
    return """
🌟 ЭЛЕГАНТНАЯ ПАРИКМАХЕРСКАЯ "СТИЛЬ И ШАРМ" 🌟
... [ваш текст о салоне] ...
"""


def main_keyboard():
    """Создаем основную клавиатуру меню"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="О нас")
    builder.button(text="Услуги")
    builder.button(text="Контакты")
    builder.button(text="Записаться")
    builder.adjust(2)  # Распределяем кнопки по 2 в ряд
    return builder.as_markup(resize_keyboard=True)


async def greet_user(message: types.Message, is_new_user: bool = True) -> None:
    greeting = "Добро пожаловать" if is_new_user else "С возвращением"
    status = "Вы успешно зарегистрированы!" if is_new_user else "Рады видеть вас снова!"
    await message.answer(
        f"{greeting}, <b>{message.from_user.full_name}</b>! {status}\n"
        "Чем я могу помочь вам сегодня?",
        reply_markup=main_keyboard()
    )


# Обработчики команд
@dp.message(Command("start"))
async def command_start_handler(message: types.Message) -> None:
    await greet_user(message)


@dp.message(lambda message: message.text == "О нас")
async def about_us_handler(message: types.Message) -> None:
    await message.answer(get_about_us_text())


@dp.message()
async def other_messages_handler(message: types.Message) -> None:
    await message.answer("Пожалуйста, используйте кнопки меню для навигации.", reply_markup=main_keyboard())


@asynccontextmanager
async def lifespan(app: FastAPI):
    webhook_url = f"{WEBHOOK_URL}{WEBHOOK_PATH}"
    try:
        await bot.set_webhook(
            url=webhook_url,
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=True
        )
        logger.info(f"Webhook установлен: {webhook_url}")
    except Exception as e:
        logger.error(f"Ошибка установки webhook: {e}")
        raise
    yield
    try:
        await bot.delete_webhook()
        logger.info("Webhook удален")
    except Exception as e:
        logger.error(f"Ошибка удаления webhook: {e}")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"status": "ok"}


@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    try:
        update = types.Update.model_validate(await request.json())
        await dp.feed_update(bot, update)
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Webhook error: {e}", exc_info=True)
        return {"status": "error"}, status.HTTP_500_INTERNAL_SERVER_ERROR
