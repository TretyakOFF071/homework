from django.urls import path
from .views import main, writers, books, book_detail

urlpatterns = [
    path('', main, name='main'),
    path('writers/', writers, name='writers'),
    path('books/', books, name='books'),
    path('books/<int:rank>', book_detail, name='book_detail')
]