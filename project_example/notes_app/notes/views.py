
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm


def notes_view(request):
    notes = Note.objects.select_related("category").all()
    categories = Category.objects.all()

    search = request.GET.get('search')
    category_id = request.GET.get('category')
    reminder = request.GET.get('reminder')

    if search:
        notes = notes.filter(title__icontains=search)

    if category_id:
        notes = notes.filter(category_id=category_id)

    if reminder:
        notes = notes.filter(reminder__date=reminder)

    return render(request, "notes_app/index.html", {
        "notes": notes,
        "categories": categories
    })


def about(request):
    return render(request, "notes_app/about.html")


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    return render(request, 'notes_app/note_form.html', {'form': form})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        if 'delete' in request.POST:
            note.delete()
            return redirect('home')

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes_app/note_detail.html', {
        'note': note,
        'form': form
    })