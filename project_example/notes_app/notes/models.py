from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes"
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="notes"
    )

    def __str__(self):
        return f"{self.title} ({self.user.username})"