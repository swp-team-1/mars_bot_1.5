from fastapi import FastAPI, Request
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import os
import uvicorn  # Добавляем для запуска сервера

app = FastAPI()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://your-project.up.railway.app

# Инициализация бота
application = Application.builder().token(TOKEN).build()

# Клавиатура для главного меню
main_keyboard = ReplyKeyboardMarkup(
    [["/ask", "/help"], ["/reload"], ["/log_in", "/log_out"]],
    resize_keyboard=True,
    one_time_keyboard=False,
)

# ===== Обработчики команд =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я бот для рекомендательных систем.",
        reply_markup=main_keyboard,
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Доступные команды:\n/ask - задать вопрос\n/help - помощь\n/reload - обновить чат\n/log_out - выйти\n/log_in - войти",
        reply_markup=main_keyboard,
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text, reply_markup=main_keyboard)

async def reload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Чат обновлен!", reply_markup=main_keyboard)

async def log_in(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Пройдите регистрацию!", reply_markup=main_keyboard)

async def log_out(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Вы вышли из аккаунта.", reply_markup=main_keyboard)

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ask_keyboard = ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True)
    await update.message.reply_text("Напишите запрос:", reply_markup=ask_keyboard)

# ===== Регистрация обработчиков =====
def register_handlers():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("reload", reload))
    application.add_handler(CommandHandler("ask", ask))
    application.add_handler(CommandHandler("log_out", log_out))
    application.add_handler(CommandHandler("log_in", log_in))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

register_handlers()

# ===== Вебхук и запуск =====
@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        update = Update.de_json(data, application.bot)
        await application.process_update(update)
        return {"status": "ok"}
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/")
async def health_check():
    return {"status": "Bot is running"}

@app.on_event("startup")
async def startup():
    await application.initialize()
    await application.bot.set_webhook(f"{WEBHOOK_URL}/webhook")

@app.on_event("shutdown")
async def shutdown():
    await application.bot.delete_webhook()
    await application.shutdown()

# Запуск сервера (важно для Railway)
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Railway использует $PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
