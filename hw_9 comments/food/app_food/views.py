from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category


def main(request, *args, **kwargs):
    return render(request, 'app_food/base.html')


def catalog(request, *args, **kwargs):
    categories = Category.objects.all()
    return render(request, 'app_food/index.html', context={'categories': categories})


def category(request, *args, **kwargs):
    products = Product.objects.filter(category__id=kwargs['pk'])
    return render(request, 'app_food/category.html', context={
        'products': products
    })
