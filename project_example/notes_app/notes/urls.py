from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    notes_view,
    about,
    note_create,
    note_detail,
)

urlpatterns = [
    path("", notes_view, name="home"),
    path("about/", about, name="about"),

    path("create/", note_create, name="note_create"),
    path("note/<int:pk>/", note_detail, name="note_detail"),

    # auth
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="notes_app/login.html"
        ),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
]