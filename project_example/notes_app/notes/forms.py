from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ("user",)
        fields = ['title', 'text', 'reminder', 'category']

        labels = {
            'title': 'Назва',
            'text': 'Текст нотатки',
            'reminder': 'Нагадування',
            'category': 'Категорія',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'reminder': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }