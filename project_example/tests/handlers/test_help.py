import pytest
from unittest.mock import AsyncMock, MagicMock
from telegram_bot.handlers.help import show_help, get_help_text
from telegram_bot.keyboards.help_links import help_links

# 1. Unit-тест для перевірки наявності критичних номерів у тексті
def test_get_help_text_contains_emergency_numbers():
    text = get_help_text()
    # Перевіряю, чи не забули головні номери
    assert "112" in text
    assert "102" in text
    assert "15-47" in text
    assert "0 800 500 335" in text
    assert "Нижче — корисні посилання" in text

# 2. Тест асинхронної функції show_help
@pytest.mark.asyncio
async def test_show_help_sends_correct_message():
    # ===== Підготовка (Mocking) =====
    update = MagicMock()
    context = MagicMock()
    
    # Створюю фейковий метод reply_text
    update.message.reply_text = AsyncMock()

    # ===== Дія =====
    await show_help(update, context)

    # ===== Перевірка =====
    # Перевіряю, що функція викликала reply_text саме з тими даними, які ми очікую
    update.message.reply_text.assert_called_once_with(
        get_help_text(),
        reply_markup=help_links
    )