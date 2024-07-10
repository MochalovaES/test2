from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Создание модели пользователя
    """
    username = None

    name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

