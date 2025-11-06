# Task_2           Writing tests for context manager

import unittest
import os
from io import StringIO
from unittest.mock import patch
from logged_open import LoggedOpen

class TestLoggedOpen(unittest.TestCase):

    def setUp(self):                                                # cтворюю тестовий файл перед кожним тестом
        self.test_filename = "test_file.txt"
        with open(self.test_filename, "w", encoding="utf-8") as f:
            f.write("Привіт, Альоно!")

    def tearDown(self):                                             # видаляю тестовий файл після кожного тесту
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    # Позитивні тести

    @patch("sys.stdout", new_callable=StringIO)
    def test_open_and_read_file(self, mock_stdout):
        with LoggedOpen(self.test_filename, "r") as f:
            content = f.read()
        self.assertIn("Привіт", content)
        self.assertTrue(f.closed)
        self.assertIn("Файл", mock_stdout.getvalue())
        self.assertGreaterEqual(LoggedOpen.open_count, 1)

    @patch("sys.stdout", new_callable=StringIO)
    def test_open_and_write_file(self, mock_stdout):
        filename = "output.txt"
        with LoggedOpen(filename, "w") as f:
            f.write("Тестовий запис")
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(f.closed)
        os.remove(filename)
        self.assertIn("закрито", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_counter_increments(self, mock_stdout):
        start = LoggedOpen.open_count
        with LoggedOpen(self.test_filename, "r"):
            pass
        self.assertEqual(LoggedOpen.open_count, start + 1)

    # Негативні тести

    @patch("sys.stdout", new_callable=StringIO)
    def test_file_not_found_error(self, mock_stdout):
        with self.assertRaises(FileNotFoundError):
            with LoggedOpen("no_such_file.txt", "r") as f:
                f.read()
        output = mock_stdout.getvalue()
        self.assertRegex(output, r"(Помилка|FileNotFoundError|not found)")

    @patch("sys.stdout", new_callable=StringIO)
    def test_error_inside_with_block(self, mock_stdout):
        def raise_error():
            raise ValueError("Щось пішло не так!")

        with self.assertRaises(ValueError):
            with LoggedOpen(self.test_filename, "r") as f:
                raise_error()
        output = mock_stdout.getvalue()
        self.assertIn("ValueError", output)

    # Додаткові перевірки
    
    def test_manual_enter_exit(self):
        obj = LoggedOpen(self.test_filename, "r")
        file_obj = obj.__enter__()
        content = file_obj.read()
        self.assertIn("Привіт", content)
        obj.__exit__(None, None, None)
        self.assertTrue(file_obj.closed)


if __name__ == "__main__":
    unittest.main()
