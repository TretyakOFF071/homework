from django.urls import path
from .views import main, brand_cars

urlpatterns = [
    path('', main, name='main'),
    path('<str:brand>/', brand_cars, name='brand_cars'),
]