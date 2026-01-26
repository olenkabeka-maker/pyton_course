import pytest
from unittest.mock import AsyncMock, MagicMock

from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.handlers.violence import handle_violence_buttons
from telegram_bot.keyboards.main_menu import main_menu

#  ===== Тестую, що буде, коли user введе невід.текс =====

@pytest.mark.asyncio
async def test_unknown_violence_text():
    #  ===== mock update =====
    update = MagicMock()
    update.message = MagicMock()
    update.message.text = "якийсь незрозумілий текст"
    update.message.reply_text = AsyncMock()

    #  ===== mock context =====
    context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)

    #  ===== виклик функції =====
    await handle_violence_buttons(update, context)

    # ===== Перевірка =====
    update.message.reply_text.assert_awaited_once_with(     # перевір.,що reply_text викликано 1 р. з точно таким текст. і з main_menu
        "Я не зовсім зрозуміла це повідомлення 🤔\n"
        "Скористайся меню 👇",
        reply_markup=main_menu
    )