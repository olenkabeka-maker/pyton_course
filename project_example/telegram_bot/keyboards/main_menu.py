from telegram import ReplyKeyboardMarkup, KeyboardButton

# ===== Кнопки головного меню =====
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🚨 Види насильства"), KeyboardButton("📝 Тестування")],
        [KeyboardButton("🆘 Куди звернутися"), KeyboardButton("ℹ️ Про бота")]
    ],
    resize_keyboard=True
)