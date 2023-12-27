from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='название категории')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='название продукта')
    price = models.FloatField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='категория')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'