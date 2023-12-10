from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=20, verbose_name='Бренд авто')
    model = models.CharField(max_length=20, verbose_name='Модель авто')
    horsepower = models.IntegerField(verbose_name='Лошадиные силы')
    year = models.IntegerField(verbose_name='Год выпуска')

    def __str__(self):
        return self.brand

