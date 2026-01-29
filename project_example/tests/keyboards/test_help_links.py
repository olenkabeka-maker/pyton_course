import pytest
from telegram import InlineKeyboardMarkup
from telegram_bot.keyboards.help_links import help_links

# Тест на тип об'єкта
def test_help_links_is_correct_type():
    # Перевіряю, що help_links дійсно є об'єктом InlineKeyboardMarkup
    assert isinstance(help_links, InlineKeyboardMarkup)

# Тест на структуру (кількість рядків та кнопок)
def test_help_links_structure():
    # У мене 2 рядки кнопок (кожна в окремих [])
    assert len(help_links.inline_keyboard) == 2
    # У кожному рядку має бути рівно по 1 кнопці
    assert len(help_links.inline_keyboard[0]) == 1
    assert len(help_links.inline_keyboard[1]) == 1

# Тест на вміст кнопок (текст та URL)
def test_help_links_content():
    # Перевіряю першу кнопку
    button_1 = help_links.inline_keyboard[0][0]
    assert button_1.text == "🆘 Нац. лінія допомоги"
    assert button_1.url == "https://la-strada.org.ua/"

    # Перевіряю другу кнопку
    button_2 = help_links.inline_keyboard[1][0]
    assert button_2.text == "🌐 Корисні ресурси"
    assert button_2.url == "https://rozirvykolo.org/"

# Тест на безпеку посилань
def test_help_links_urls_are_secure():
    for row in help_links.inline_keyboard:
        for button in row:
            # Перевіряю, що всі посилання починаються з https://
            assert button.url.startswith("https://"), f"Посилання {button.url} має бути безпечним (https)"