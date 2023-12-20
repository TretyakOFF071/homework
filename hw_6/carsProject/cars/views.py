from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars


def main(request, *args, **kwargs):
    return render(request, 'cars/base.html')


def brand_cars(request, brand):
    car = Cars.objects.get(brand=brand)
    return render(request, 'cars/detail.html', context={'car': car})