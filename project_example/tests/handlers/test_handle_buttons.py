import pytest
from unittest.mock import AsyncMock, MagicMock

from telegram_bot.bot import handle_buttons
from telegram_bot.keyboards.violence_menu import violence_menu
from telegram_bot.keyboards.main_menu import main_menu
from telegram_bot.keyboards.test_links import test_links
from telegram_bot.handlers.violence import get_violence_text

# ===== Тест "🚨 Види насильства" =====
@pytest.mark.asyncio                                    # @pytest.mark.asyncio - тестує async def
async def test_handle_buttons_violence_menu():

    # ===== Підготовка =====
    update = MagicMock()
    context = MagicMock()

    update.message.text = "🚨 Види насильства"
    update.message.reply_text = AsyncMock()             # AsyncMock() - бо reply_text — async-функція

    # ===== Дія =====
    await handle_buttons(update, context)

    # ===== Перевірка =====
    update.message.reply_text.assert_called_once_with(  #.assert_called_once_with -перевірю, щоб ф-ія виклик. 1 р., з точним текстом, з правильною клавіатурою
        get_violence_text(),
        reply_markup=violence_menu
    )

# ===== Тест "⬅️ назад" =====
@pytest.mark.asyncio
async def test_handle_buttons_back_to_main_menu():
    # ===== Підготовка =====
    update = MagicMock()
    context = MagicMock()

    update.message.text = "⬅️ назад"
    update.message.reply_text = AsyncMock()

    # ===== Дія =====
    await handle_buttons(update, context)

    # ===== Перевірка =====
    update.message.reply_text.assert_called_once_with(
        "Повертаємося в головне меню",
        reply_markup=main_menu
    )

# ===== Тест "📝 Тестування" =====
@pytest.mark.asyncio
async def test_handle_buttons_testing_links():
    # ===== Підготовка =====
    update = MagicMock()
    context = MagicMock()

    update.message.text = "📝 Тестування"
    update.message.reply_text = AsyncMock()

    # ===== Дія =====
    await handle_buttons(update, context)

    # ===== Перевірка =====
    update.message.reply_text.assert_called_once_with(
        "📝 Це тестування допоможе вам визначити, чи є ознаки насильства у ваших стосунках 💔\n\n"
        "Якщо тебе цікавить - натисни нижче 👇",
        reply_markup=test_links
    )