# тут я підключаю токен
import os
from dotenv import load_dotenv

# Завантажую змінні з .env
load_dotenv()

# Беру токен з .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from keyboards.main_menu import main_menu
from keyboards.violence_menu import violence_menu
from handlers.violence import get_violence_text, get_detailed_text
from handlers.help import get_help_text
from texts.violence_texts import violence_texts

#  Створюю бота
application = ApplicationBuilder().token(BOT_TOKEN).build()

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт 💙\n"
        "Я допоможу розпізнати різні види насильства та підкажу, куди звернутися.\n\n"
        "Обери, що тебе цікавить 👇",
        reply_markup=main_menu
    )

# ===== Обробка підменю насильства =====
async def handle_violence_buttons(update, context):
    text = update.message.text.lower()              # переведемо в нижній регістр для збігу
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

# ===== Обробка головного меню та підменю =====
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚨 Види насильства":
        await update.message.reply_text(get_violence_text(), reply_markup=violence_menu)
    elif text == "🆘 Куди звернутися":
        await update.message.reply_text(get_help_text(), reply_markup=main_menu)
    elif text == "ℹ️ Про бота":
        await update.message.reply_text(
            "Цей бот створений, щоб підтримати тебе 💙\n"
            "Ти не винна / не винен у насильстві.\n"
            "Допомога існує.",
            reply_markup=main_menu
        )
    else:
        # Передаємо обробку підменю насильства
        await handle_violence_buttons(update, context)

# ===== Точка входу =====
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Додаємо хендлери
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Бот запущений ✅")
    app.run_polling()

if __name__ == "__main__":
    main()