# ===== Тест: жінка → "F" =====

import pytest
from unittest.mock import AsyncMock, MagicMock
from telegram_bot.bot import gender, AGE, GENDER_FEMALE, GENDER_MALE


@pytest.mark.asyncio
async def test_gender_female():
    # ===== Підготовка =====
    update = MagicMock()
    update.message = MagicMock()
    update.message.text = GENDER_FEMALE[0]
    update.message.reply_text = AsyncMock()

    context = MagicMock()
    context.user_data = {}

    # ===== Дія =====
    result = await gender(update, context)

    # ===== Перевірка =====
    assert context.user_data["gender"] == "F"

    update.message.reply_text.assert_awaited_once_with(
        "Вкажи свій вік цифрами:"
    )

    assert result == AGE

# ===== Тест: чоловік → "M" =====

@pytest.mark.asyncio
async def test_gender_male():
    update = MagicMock()
    update.message = MagicMock()
    update.message.text = GENDER_MALE[0]
    update.message.reply_text = AsyncMock()

    context = MagicMock()
    context.user_data = {}

    result = await gender(update, context)

    assert context.user_data["gender"] == "M"
    assert result == AGE

# ===== Тест: некоректне значення → "NA" =====

@pytest.mark.asyncio
async def test_gender_unknown():
    # ===== Підготовка =====
    update = MagicMock()
    update.message.text = "🐱"
    update.message.reply_text = AsyncMock()

    context = MagicMock()
    context.user_data = {}

    # ===== Дія =====
    from telegram_bot.bot import GENDER
    result = await gender(update, context)

    # ===== Перевірка =====
    # Тепер ми перевіряємо, що в user_data НІЧОГО не записалося
    assert "gender" not in context.user_data
    
    # Перевіряємо, що бот попросив уточнити
    update.message.reply_text.assert_called_once_with("Будь ласка, введи Ж або Ч")
    
    # Перевіряємо, що ми залишилися на етапі вибору статі (GENDER)
    assert result == GENDER

