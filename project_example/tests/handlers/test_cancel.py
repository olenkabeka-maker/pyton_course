import pytest
from unittest.mock import AsyncMock, MagicMock
from telegram_bot.bot import cancel, ConversationHandler

@pytest.mark.asyncio
async def test_cancel_command_sends_message_and_ends_conv():
    # ===== Підготовка (Mocking) =====
    update = MagicMock()
    context = MagicMock()
    
    # Мокаю reply_text, оскільки це асинхронна функція
    update.message.reply_text = AsyncMock()

    # ===== Дія (Викликаю функцію) =====
    result = await cancel(update, context)

    # ===== Перевірка =====
    # 1. Чи отримав користувач правильне повідомлення про скасування
    update.message.reply_text.assert_called_once_with(
        "Ви відмінили введення статистики."
    )
    
    # 2. Чи повертає функція сигнал про завершення розмови
    # У Telegram ConversationHandler.END зазвичай дорівнює -1
    assert result == ConversationHandler.END
