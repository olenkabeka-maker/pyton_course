from django.test import TestCase
from django.utils import timezone

from .models import Note, Category
from .forms import NoteForm


class CategoryModelTest(TestCase):

    def test_create_category(self):
        category = Category.objects.create(title="Робота")

        self.assertEqual(category.title, "Робота")
        self.assertEqual(str(category), "Робота")


class NoteModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Особисте")

    def test_create_note(self):
        note = Note.objects.create(
            title="Моя нотатка",
            text="Текст нотатки",
            reminder=timezone.now(),
            category=self.category
        )

        self.assertEqual(note.title, "Моя нотатка")
        self.assertEqual(note.text, "Текст нотатки")
        self.assertEqual(note.category.title, "Особисте")
        self.assertIsNotNone(note.reminder)

    def test_update_note(self):
        note = Note.objects.create(
            title="Стара назва",
            text="Старий текст",
            category=self.category
        )

        note.title = "Нова назва"
        note.text = "Новий текст"
        note.save()

        note.refresh_from_db()

        self.assertEqual(note.title, "Нова назва")
        self.assertEqual(note.text, "Новий текст")

    def test_note_str_method(self):
        note = Note.objects.create(
            title="Тест",
            text="Текст",
            category=self.category
        )

        self.assertEqual(str(note), f"Тест {note.id}")


class NoteFormTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Навчання")

    def test_form_valid_data(self):
        form = NoteForm(data={
            "title": "Нова нотатка",
            "text": "Важливий текст",
            "reminder": timezone.now().strftime("%Y-%m-%dT%H:%M"),
            "category": self.category.id
        })

        self.assertTrue(form.is_valid())

    def test_form_without_reminder(self):
        form = NoteForm(data={
            "title": "Без нагадування",
            "text": "Текст",
            "category": self.category.id
        })

        self.assertTrue(form.is_valid())

    def test_form_invalid_without_category(self):
        form = NoteForm(data={
            "title": "Без категорії",
            "text": "Текст"
        })

        self.assertFalse(form.is_valid())
        self.assertIn("category", form.errors)