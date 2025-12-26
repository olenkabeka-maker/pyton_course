
from django.shortcuts import render

def notes_view(request):
    notes = [
        {"title": "Перша нотатка", "text": "Купити молоко"},
        {"title": "Друга нотатка", "text": "Повторити Django"},
        {"title": "Третя нотатка", "text": "Прогулянка з собакою"}
    ]

    return render(request, "notes_app/index.html", {"notes": notes})