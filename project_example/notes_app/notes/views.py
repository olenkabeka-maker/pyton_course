
from django.shortcuts import render
from .models import Note


def notes_view(request):
    notes = Note.objects.select_related("category").all()

    return render(request, "notes_app/index.html", {
        "notes": notes
    })

def about(request):
    return render(request, "notes_app/about.html") 