from django.db import models


import uuid


class Key(models.Model):
    class Meta:
        verbose_name = 'Ключ'
        verbose_name_plural = 'Ключи'

    key = models.CharField(max_length=200, verbose_name='Ключ')

    def __str__(self):
        return '{}'.format(self.key)


class App(models.Model):
    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'

    name = models.CharField(max_length=200, verbose_name='Имя')
    key = models.OneToOneField(Key,
                               on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{} {}'.format(self.id, self.name, self.key)
