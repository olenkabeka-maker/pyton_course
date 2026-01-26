import pytest
from unittest.mock import AsyncMock, MagicMock

from telegram_bot.bot import start
from telegram_bot.keyboards.main_menu import main_menu

# ===== Тест start/ ===== 
@pytest.mark.asyncio                                    # @pytest.mark.asyncio - тестує async def
async def test_start_command_sends_welcome_message():
    # ===== Підготовка ===== 
    update = MagicMock()                                # MagicMock() - фейковий об’єкт замість Update, Context
    context = MagicMock()

    update.message.reply_text = AsyncMock()             # AsyncMock() - бо reply_text — async-функція

    # ===== Дія =====
    await start(update, context)

    # ===== Перевірка =====
    update.message.reply_text.assert_called_once_with(  #.assert_called_once_with -перевірю, щоб ф-ія виклик. 1 р., з точним текстом, з правильною клавіатурою
        "Привіт 💙\n"
        "Я допоможу розпізнати різні види насильства та підкажу, куди звернутися.\n\n"
        "Обери, що тебе цікавить 👇",
        reply_markup=main_menu
    )