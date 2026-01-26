

from django.contrib.auth.models import User
from .models import AnonymousStat, Note, Category


def update_statistics_note():
    stats = AnonymousStat.objects.all()
    total = stats.count()

    if total == 0:
        content = "Ще немає зібраної статистики."
    else:
        females = stats.filter(gender="F").count()
        males = stats.filter(gender="M").count()
        na = stats.filter(gender="NA").count()
        avg_age = round(sum(s.age for s in stats) / total, 1)

        content = (
            f"📊 Статистика користувачів бота\n\n"
            f"Усього записів: {total}\n"
            f"Жінки: {females}\n"
            f"Чоловіки: {males}\n"
            f"Не вказано: {na}\n"
            f"Середній вік: {avg_age}"
        )

    # ⚠️ цей користувач має існувати в адмінці
    user = User.objects.get(username="statistics_bot")

    category, _ = Category.objects.get_or_create(title="Системні")

    note, _ = Note.objects.get_or_create(
        user=user,
        title="Статистика користувачів",
        defaults={"category": category}
    )

    note.text = content
    note.save()