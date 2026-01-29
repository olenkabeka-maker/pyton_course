import pytest
from unittest.mock import AsyncMock, MagicMock

from telegram_bot.bot import start

# ===== Тест start/ ===== 
@pytest.mark.asyncio                                    # @pytest.mark.asyncio - тестує async def
async def test_start_asks_for_gender():
    # ===== Підготовка ===== 
    update = MagicMock()                                # MagicMock() - фейковий об’єкт замість Update, Context
    update.message = MagicMock()
    update.message.reply_text = AsyncMock()             # AsyncMock() - бо reply_text — async-функція
   
    context = MagicMock()
    # ===== Дія =====
    result = await start(update, context)

    # ===== Перевірка =====
    update.message.reply_text.assert_awaited_once_with(  #.assert_awaited_once_with -перевірю, що ф-цію виклик. 1 р., з точними аргументами
        "Привіт 💙\nЩоб покращити статистику, скажи будь ласка свою стать (Ж/Ч)"
    )
    # ===== Перевірка стану =====
    assert result == 0   # GENDER