from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.


def cur_time(request, *args, **kwargs):

    context = {
        'date_now': datetime.datetime.now()
    }

    return render(request, 'current_time/index.html', context=context)