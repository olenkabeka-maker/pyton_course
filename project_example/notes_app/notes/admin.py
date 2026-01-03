from django.contrib import admin
from .models import Note, Category

@admin.action(description="Update remainder")
def delete_remainder(modeladmin, request, queryset):
    queryset.update(reminder="2026-02-02")

class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "reminder", "category"]
    list_filter = ["category"]
    actions = [delete_remainder]

admin.site.register(Note, NoteAdmin)
admin.site.register(Category)
