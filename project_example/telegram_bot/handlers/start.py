from telegram import ReplyKeyboardMarkup
from keyboards.main_menu import main_menu

# ===== Функція для відповіді на /start =====
async def start(update, context):
    await update.message.reply_text(
        "Привіт 💙\n"
        "Я допоможу розпізнати різні види насильства та підкажу, куди звернутися по допомогу.\n\n"
        "Обери, що тебе цікавить 👇",
        reply_markup=main_menu
    )