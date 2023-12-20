from django.urls import path
from .views import main, detail_page

urlpatterns = [
    path('', main, name='main'),
    path('<str:model>/', detail_page, name='detail_page'),
]

# path('detail/', detail_page, name='detail_page'),