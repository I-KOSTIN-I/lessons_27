from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.TextField(max_length=300)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = [
        (MEMBER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=9, choices=ROLES, default='member')
    age = models.PositiveIntegerField(null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
