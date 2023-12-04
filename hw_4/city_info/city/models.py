from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title}'

class Management(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    title = models.TextField(verbose_name='Должность')

    def __str__(self):
        return f'{self.name}'


class Facts(models.Model):

    title = models.CharField(max_length=30, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Факт')

    def __str__(self):
        return f'{self.title}'

class Contacts(models.Model):
    name = models.CharField(max_length=30, verbose_name='Контакт')
    number = models.TextField(verbose_name='Номер')

    def __str__(self):
        return f'{self.name}'