import pytest
import requests
from unittest.mock import AsyncMock, MagicMock, patch
from telegram_bot.bot import age, ConversationHandler

@pytest.mark.asyncio
async def test_age_success_and_api_call():
    # Підготовка
    update = MagicMock()
    update.message.text = "25"                  # user ввів число
    update.message.reply_text = AsyncMock()
    
    context = MagicMock()
    context.user_data = {"gender": "F"}         # Дані з попереднього кроку

    # Мокаємо requests.post, щоб він не ліз в інтернет, а повертав "201 Created"
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 201
        
        result = await age(update, context)

        # Перевірка: чи дані збереглися в user_data
        assert context.user_data["age"] == 25
        # Перевірка: чи функція завершила розмову
        assert result == ConversationHandler.END
        # Перевірка: чи був викликаний API з правильними даними
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        assert kwargs['json'] == {"gender": "F", "age": 25}

@pytest.mark.asyncio
async def test_age_invalid_input():
    update = MagicMock()
    update.message.text = "сорок"               # Помилка: текст замість цифр
    update.message.reply_text = AsyncMock()
    context = MagicMock()

    result = await age(update, context)

    # Перевірка: бот має попросити спробувати ще раз і повернути стан AGE
    assert result == 1 # AGE
    update.message.reply_text.assert_called_with("Вік потрібно вказати числом, спробуй ще раз:")


# ===== Тест на помилку з’єднання =====

@pytest.mark.asyncio
async def test_age_api_connection_error():
    # ===== Підготовка =====
    update = MagicMock()
    update.message.text = "25"
    update.message.reply_text = AsyncMock()
    
    context = MagicMock()
    context.user_data = {"gender": "F"}

    with patch('requests.post') as mock_post:
        # Імітує помилку з'єднання
        mock_post.side_effect = requests.exceptions.ConnectionError("Failed to connect")

        # ===== Дія =====
        result = await age(update, context)

        # ===== Перевірка  =====
        # 1. Отримує список усіх викликів reply_text
        calls = update.message.reply_text.call_args_list
        
        # Перевіряє, чи було рівно два повідомлення
        assert len(calls) == 2

        # 2. Перевіряє перше повідомлення (про помилку)
        # calls[0][0] — це аргументи першого виклику
        assert "Помилка з’єднання з сервером" in calls[0][0][0]

        # 3. Перевіряє друге повідомлення (головне меню)
        assert "Обери, що тебе цікавить 👇" in calls[1][0][0]
        
        # 4. Перевіряє, що функція повернула END
        assert result == ConversationHandler.END