from django.db import models

class Ingredient(models.Model):

    name = models.CharField(max_length=20, unique=True, verbose_name='название ингредиента')
    ingredient_amount = models.FloatField(verbose_name='грамм')

    class Meta:

        db_table = 'ingredient'
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return f'{self.name}'



class Meal(models.Model):

    name = models.CharField(max_length=20, unique=True, verbose_name='название блюда')
    price = models.FloatField(verbose_name='цена блюда')
    ingredient = models.ManyToManyField(Ingredient, verbose_name='ингредиенты',
                                        related_name='meals')

    class Meta:

        db_table = 'meal'
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self):
        return f'{self.name}'
