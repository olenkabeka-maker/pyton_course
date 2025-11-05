# Task_2
"""Write tests for the Phonebook application, which you have implemented in module 1. 
Design tests for this solution and write tests using unittest library"""

import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import json
import phonebook

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "phones": [
                {"name": "Альона", "lastName": "Лащенко", "phone": "123", "city": "Київ"},
                {"name": "Настя", "lastName": "Іваненко", "phone": "456", "city": "Львів"}
            ]
        }

    # ------------------ load_phonebook ------------------
    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='{"phones": []}')
    def test_load_phonebook_success(self, mock_file, mock_exists):
        # Патчимо os.path.exists -> True і open -> JSON
        result = phonebook.load_phonebook("test.json")
        self.assertIn("phones", result)

    @patch("os.path.exists", return_value=False)
    def test_load_phonebook_file_not_found(self, mock_exists):
        # Якщо файл не існує — функція викликає sys.exit(1)
        with self.assertRaises(SystemExit) as cm:
            phonebook.load_phonebook("no_file.json")
        # перевіримо код виходу = 1
        self.assertEqual(cm.exception.code, 1)

    # ------------------ save_phonebook ------------------
    @patch("builtins.open", new_callable=mock_open)
    @patch("sys.stdout", new_callable=StringIO)
    def test_save_phonebook(self, mock_stdout, mock_file):
        phonebook.save_phonebook("test.json", self.sample_data)
        output = mock_stdout.getvalue()
        self.assertIn("Дані збережено", output)

    # ------------------ add_entry ------------------
    @patch("builtins.input", side_effect=["Іра", "Коваль", "789", "Одеса"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_entry(self, mock_stdout, mock_input):
        pb = {"phones": []}
        phonebook.add_entry(pb)
        self.assertEqual(len(pb["phones"]), 1)
        self.assertEqual(pb["phones"][0]["city"], "Одеса")
        self.assertIn("Запис додано", mock_stdout.getvalue())

    # ------------------ search_by_first_name ------------------
    @patch("builtins.input", return_value="Альона")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_by_first_name_found(self, mock_stdout, mock_input):
        phonebook.search_by_first_name(self.sample_data)
        output = mock_stdout.getvalue()
        self.assertIn("Знайдено", output)
        self.assertIn("Альона", output)

    @patch("builtins.input", return_value="Марія")
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_by_first_name_not_found(self, mock_stdout, mock_input):
        phonebook.search_by_first_name(self.sample_data)
        self.assertIn("Нічого не знайдено", mock_stdout.getvalue())

    # ------------------ delete_by_phone ------------------
    @patch("builtins.input", side_effect=["123", "y"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_by_phone_found(self, mock_stdout, mock_input):
        pb = {"phones": [{"name": "Альона", "lastName": "Лащенко", "phone": "123", "city": "Київ"}]}
        phonebook.delete_by_phone(pb)
        self.assertEqual(len(pb["phones"]), 0)
        self.assertIn("Запис видалено", mock_stdout.getvalue())

    @patch("builtins.input", return_value="999")
    @patch("sys.stdout", new_callable=StringIO)
    def test_delete_by_phone_not_found(self, mock_stdout, mock_input):
        phonebook.delete_by_phone(self.sample_data)
        self.assertIn("Запис не знайдено", mock_stdout.getvalue())



if __name__ == "__main__":
    unittest.main()