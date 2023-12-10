from django.db import models

class Toyota(models.Model):
    model = models.CharField(max_length=20, verbose_name='Модель авто')
    horsepower = models.IntegerField(verbose_name='Лошадиные силы')
    year = models.IntegerField(verbose_name='Год выпуска')

class Honda(models.Model):
    model = models.CharField(max_length=20, verbose_name='Модель авто')
    horsepower = models.IntegerField(verbose_name='Лошадиные силы')
    year = models.IntegerField(verbose_name='Год выпуска')

class Renault(models.Model):
    model = models.CharField(max_length=20, verbose_name='Модель авто')
    horsepower = models.IntegerField(verbose_name='Лошадиные силы')
    year = models.IntegerField(verbose_name='Год выпуска')