# для кнопки з посиланням на тестування

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

test_links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                "📝 Пройти тест",
                url="https://rozirvykolo.org/pereviriti-stosunki/"  #  посилання на тестування
            )
        ]
    ]
)