from telegram import ReplyKeyboardMarkup, KeyboardButton

violence_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("👊 Фізичне"), KeyboardButton("🧠 Психологічне")],
        [KeyboardButton("💰 Економічне"), KeyboardButton("🔞 Сексуальне")],
        [KeyboardButton("⬅️ Назад")]
    ],
    resize_keyboard=True
)