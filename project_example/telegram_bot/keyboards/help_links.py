from telegram import InlineKeyboardButton, InlineKeyboardMarkup

help_links = InlineKeyboardMarkup(                    # inline-кнопки з посиланнями
    inline_keyboard=[
        [
            InlineKeyboardButton(
                "🆘 Нац. лінія допомоги",
                url="https://la-strada.org.ua/"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Корисні ресурси",
                url="https://rozirvykolo.org/"
            )
        ]
    ]
)