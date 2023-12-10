from django.shortcuts import render
from django.http import HttpResponse
from .models import Toyota, Renault, Honda


def main(request, *args, **kwargs):
    return render(request, 'cars/base.html')
def toyota(request, *args, **kwargs):
    toyota = Toyota.objects.all()
    return render(request, 'cars/toyota.html', context={'toyota': toyota})

def honda(request, *args, **kwargs):
    honda = Honda.objects.all()
    return render(request, 'cars/honda.html', context={'honda': honda})

def renault(request, *args, **kwargs):
    renault = Renault.objects.all()
    return render(request, 'cars/renault.html', context={'renault': renault})