from django.db import models

# Create your models here.

class Writer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя автора')
    birth_date = models.TextField(verbose_name='Дата роджения')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    publication_date = models.TextField(verbose_name='Дата публикации')
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, verbose_name='Автор')
    rank = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.title