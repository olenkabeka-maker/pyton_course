from telegram_bot.texts.violence_texts import violence_texts
from telegram_bot.keyboards.main_menu import main_menu
from telegram_bot.keyboards.violence_menu import violence_menu

# Повертає короткий текст + кнопки підменю
def get_violence_text():
    return (
        "Насильство буває різним:\n"
        "Обери тип насильства, щоб дізнатися детальніше 👇"
    )

# Повертає детальний текст по кожному виду
def get_detailed_text(violence_type: str):
    return violence_texts.get(violence_type.lower(), "Інформація відсутня")

# Обробка підменю кнопок
async def handle_violence_buttons(update, context):
    if not update.message or not update.message.text:       # захист
        return

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
        await update.message.reply_text(                    # якщо юзер ввів незрозумілий текст
            "Я не зовсім зрозуміла це повідомлення 🤔\n"
            "Скористайся меню 👇",
            reply_markup=main_menu
        )