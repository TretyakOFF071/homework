from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Writer, Book


def main(request, *args, **kwargs):
    return render(request, 'app_writers/base.html')
def writers(request, *args, **kwargs):
    writers = Writer.objects.all()
    return render(request, 'app_writers/writers.html', context={'writers': writers})


def books(request, *args, **kwargs):
    books = Book.objects.all()
    return render(request, 'app_writers/books.html', context={'books': books})

def book_detail(request, rank):
    book = Book.objects.get(rank=rank)
    if book.rank > 5:
        return redirect('books')
    else:
        return render(request, 'app_writers/book_detail.html', context={'book': book})




