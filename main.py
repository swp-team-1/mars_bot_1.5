from fastapi import FastAPI, Request
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes, ConversationHandler,
)
import os
import uvicorn  # Добавляем для запуска сервера
import requests



app = FastAPI()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Пример: https://your-project.up.railway.app

# Инициализация бота
application = Application.builder().token(TOKEN).build()

# Клавиатура для главного меню
main_keyboard = ReplyKeyboardMarkup(
    [["/ask", "/help"]],
    resize_keyboard=True,
    one_time_keyboard=False,
)

# ===== Обработчики команд =====
START, GET_NAME1 = range(2)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Привет! Я бот для рекомендательных систем.",
        reply_markup=main_keyboard,
    )
    api_check_user = f"https://swpdb-production.up.railway.app/users/{update.effective_user.id}/"
    if requests.get(api_check_user).status_code == 200:
        await update.message.reply_text(
            "Вы уже зарегистрированы!",
            reply_markup=main_keyboard,
        )
        return ConversationHandler.END
    await update.message.reply_text(
        "Пожалуйста, введите ваше имя: ",
        reply_markup=main_keyboard,
    )
    return GET_NAME1
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Получение и сохранение имени пользователя"""
    user_name = update.message.text
    context.user_data['name'] = user_name  # Сохраняем имя

    await update.message.reply_text(
        f"Отлично, {user_name}! Теперь вы можете пользоваться ботом.",
        reply_markup=main_keyboard,
    )
    payload_name_json = {
        "_id" : update.effective_user.id,
        "name" : user_name,
    }
    api_create_user = "https://swpdb-production.up.railway.app/users/"
    response_name = requests.post(api_create_user, json=payload_name_json)
    if response_name.status_code == 200:
        print("yra")
    else:
        print("no")

    return ConversationHandler.END
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отмена ввода имени"""
    await update.message.reply_text(
        "Отмена",
        reply_markup=main_keyboard,
    )

    return ConversationHandler.END


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Доступные команды:\n/ask - задать вопрос\n/help - помощь",
        reply_markup=main_keyboard,
    )

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(update.message.text, reply_markup=main_keyboard)



async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ask_keyboard = ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True)
    await update.message.reply_text("Напишите запрос:", reply_markup=ask_keyboard)

# ===== Регистрация обработчиков =====
def register_handlers():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CommandHandler("ask", ask))


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
