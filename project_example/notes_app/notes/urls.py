from django.urls import path
from .views import (
    notes_view,
    about,
    note_create,
    note_detail
)

urlpatterns = [
    path("", notes_view, name="home"),
    path("about/", about, name="about"),

    path("create/", note_create, name="note_create"),
    path("note/<int:pk>/", note_detail, name="note_detail"),
]