from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """User profile: just minimum."""

    tlg_name = models.CharField(
        max_length=256,
        verbose_name='ФИО пользователя',
    )
    tlg_id = models.PositiveBigIntegerField(
        verbose_name='ID диалога пользователя',
        db_index=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
        help_text='Дата и время добавления, автоматически'
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name
