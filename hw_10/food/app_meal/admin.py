from django.contrib import admin
from .models import Ingredient, Meal

class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'ingredient_amount']


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Meal, MealAdmin)





