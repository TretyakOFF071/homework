from django.db import models


class Headphone(models.Model):
    model = models.CharField(max_length=20, verbose_name='Модель наушников')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    charge = models.CharField(max_length=20,verbose_name='Время работы')

    def __str__(self):
        return self.model