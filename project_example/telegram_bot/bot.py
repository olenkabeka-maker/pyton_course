# тут я підключаю токен
import os
from dotenv import load_dotenv
import logging
import requests

from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ContextTypes, ConversationHandler
)

from telegram_bot.keyboards.main_menu import main_menu
from telegram_bot.keyboards.test_links import test_links
from telegram_bot.keyboards.violence_menu import violence_menu

from telegram_bot.handlers.violence import get_violence_text, get_detailed_text
from telegram_bot.handlers.help import show_help
from telegram_bot.texts.violence_texts import violence_texts

# ===== Завантажуємо токен =====
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ===== Логування =====
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ===== Стани для ConversationHandler =====
GENDER, AGE = range(2)
API_URL = "http://127.0.0.1:8000/api/statistics/"

# ================================
# ===== ФУНКЦІЇ БОТА ============
# ================================

# /start — початок статистики
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"/start від користувача {update.effective_user.id}")
    await update.message.reply_text(
        "Привіт 💙\nЩоб покращити статистику, скажи будь ласка свою стать (Ж/Ч)"
    )
    return GENDER

# Обробка статі
async def gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text in ["ж", "жінка", "f"]:
        context.user_data["gender"] = "F"
    elif text in ["ч", "чоловік", "m"]:
        context.user_data["gender"] = "M"
    else:
        context.user_data["gender"] = "NA"

    await update.message.reply_text("Вкажи свій вік цифрами:")
    return AGE

# Обробка віку
async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        age = int(update.message.text)
        context.user_data["age"] = age
    except ValueError:
        await update.message.reply_text("Вік потрібно вказати числом, спробуй ще раз:")
        return AGE

    # Відправляємо на Django API
    payload = {
        "gender": context.user_data["gender"],
        "age": context.user_data["age"]
    }
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 201:
            await update.message.reply_text("Дякую! Твоя анонімна статистика збережена.")
        else:
            await update.message.reply_text("Щось пішло не так, статистику не збережено.")
    except Exception as e:
        await update.message.reply_text(f"Помилка з’єднання з сервером: {e}")

    # Після статистики показуємо головне меню
    await update.message.reply_text(
        "Обери, що тебе цікавить 👇",
        reply_markup=main_menu
    )
    return ConversationHandler.END

# /cancel — відміна
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ви відмінили введення статистики.")
    return ConversationHandler.END

# ===== Обробка головного меню та підменю насильства =====
async def handle_violence_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text in violence_texts:
        await update.message.reply_text(
            get_detailed_text(text),
            reply_markup=violence_menu
        )
    elif text == "⬅️ назад":
        await update.message.reply_text(
            "Повертаємося в головне меню",
            reply_markup=main_menu
        )
    else:
        await update.message.reply_text(
            "Я не зовсім зрозуміла це повідомлення 🤔\nСкористайся меню 👇",
            reply_markup=main_menu
        )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚨 Види насильства":
        await update.message.reply_text(get_violence_text(), reply_markup=violence_menu)
    elif text == "ℹ️ Про бота":
        await update.message.reply_text(
            "Цей бот створений, щоб підтримати тебе 💙\n"
            "Ти не винна / не винен у насильстві.\nДопомога існує.",
            reply_markup=main_menu
        )
    elif text == "📝 Тестування":
        await update.message.reply_text(
            "📝 Це тестування допоможе вам визначити, чи є ознаки насильства у ваших стосунках 💔\n\n"
            "Якщо тебе цікавить - натисни нижче 👇",
            reply_markup=test_links
        )
    else:
        await handle_violence_buttons(update, context)

# ================================
# ===== MAIN =====================
# ================================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ConversationHandler для збору статистики
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            GENDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, gender)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, age)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    app.add_handler(conv_handler)

    # Інші MessageHandler для кнопок
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^🆘 Куди звернутися$"), show_help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Бот запущений ✅")
    app.run_polling()

if __name__ == "__main__":
    main()