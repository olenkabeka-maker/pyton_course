
from django.http import HttpResponse

def notes_view(request):
    return HttpResponse("Привіт із програми Notes")