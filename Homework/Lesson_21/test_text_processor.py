# тести з pytest, із використанням фікстури @pytest.fixture

import pytest
from logged_open import LoggedOpen
from text_processor import process_text


@pytest.fixture                             # фікстура pytest - створює тестовий файл і повертає файловий об'єкт через LoggedOpen
def sample_file(tmp_path):                  # cтворює тимч. файл і відкриває його через LoggedOpen
   
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Привіт, Альоно! Це тестовий файл із кількома словами.", encoding="utf-8")

    with LoggedOpen(test_file, "r") as f:   # повертає файловий об’єкт через LoggedOpen
        yield f                             # повертає ресурс тесту, після чого pytest сам виконає clean-up


def test_process_text_counts_words_correctly(sample_file):          # тест для process_text()
    result = process_text(sample_file)
    assert result == 8, f"Очікувалось 8 слів, отримано {result}"


def test_process_text_empty_file(tmp_path):                         # тест із порожнім файлом
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("", encoding="utf-8")

    with LoggedOpen(empty_file, "r") as f:
        result = process_text(f)
    assert result == 0