from django.urls import path
from .views import cur_time

urlpatterns = [
    path('', cur_time, name='cur_time')
]