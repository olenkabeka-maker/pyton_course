from django.urls import path
from .views import notes_view, about

urlpatterns = [
    path("", notes_view, name="home"),
    path("about/", about, name="about"),
]