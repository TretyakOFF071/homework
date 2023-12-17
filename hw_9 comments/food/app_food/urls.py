from django.urls import path
from .views import main, catalog, category

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('', main, name='main'),
    path('catalog/category/<int:pk>/', category, name='category')
]
