from django.urls import path
from .views import add_restaurant, restaurant_list, restaurant_delete, restaurant_edit

urlpatterns = [
    path('add/', add_restaurant, name='add_restaurant'),
    path('', restaurant_list, name='restaurant_list'),
    path('<int:pk>/delete/', restaurant_delete, name='delete_restaurant'),
    path('<int:pk>/edit/', restaurant_edit, name='restaurant_edit'),
]