from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser, models.Model):

    phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Номер телефона')
    birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        ordering = ("-pk",)