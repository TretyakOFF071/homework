from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Management, Facts, Contacts

# Create your views here.

def main(request, *args, **kwargs):
    return render(request, 'city/base.html')

def news(request, *args, **kwargs):
    news = News.objects.all()
    return render(request, 'city/news.html', context={'news': news})

def management(request, *args, **kwargs):
    managements = Management.objects.all()
    return render(request, 'city/management.html', context={'managements': managements})

def facts(request, *args, **kwargs):
    facts = Facts.objects.all()
    return render(request, 'city/facts.html', context={'facts': facts})

def contacts(request, *args, **kwargs):
    contacts = Contacts.objects.all()
    return render(request, 'city/contacts.html', context={'contacts': contacts})