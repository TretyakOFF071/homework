from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def programmer_day(request):
    current_year = datetime.now().year
    programmer_day = datetime(current_year, 1, 1) + timedelta(256)
    context = {'programmer_day': programmer_day.strftime('%Y-%m-%d')}
    return render(request, 'app_day/index.html', context=context)