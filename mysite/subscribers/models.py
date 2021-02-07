from django.db import models

# Create your models here.

class Subscriber(models.Model):
    """Модель подписчика Subscribers"""
    email = models.CharField('Email', max_length=100, blank=False, null=False, help_text='Веедите Ваш email')
    full_name = models.CharField('Имя Фамилия', max_length=100, blank=False, null=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'