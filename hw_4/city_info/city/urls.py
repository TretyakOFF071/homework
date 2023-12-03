from django.urls import path
from .views import main, news, contacts, management, facts

urlpatterns = [
    path('', main, name='main'),
    path('news/', news, name='news'),
    path('contacts/', contacts, name='contacts'),
    path('management/', management, name='management'),
    path('facts/', facts, name='facts')
]