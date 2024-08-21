from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Movie

@receiver(post_save, sender=Movie)
def send_new_movie_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый фильм добавлен: {instance.title}'
        message = f'Фильм "{instance.title}" был добавлен в базу данных.\n\nОписание: {instance.description}'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )