from django.shortcuts import render, redirect
from .models import Headphone

def main(request):
    return render(request, 'app_headphones/main.html')


def detail_page(request, *args, **kwargs):
    model = kwargs.get('model')
    try:
        headphone = Headphone.objects.get(model=model)
    except Headphone.DoesNotExist:
        return redirect('main')
    return render(request, 'app_headphones/detail.html', context={'headphone': headphone})


# def detail_page(request, *args, **kwargs):
#     model = request.GET.get('model', '')
#     try:
#         headphone = Headphone.objects.get(model=model)
#     except Headphone.DoesNotExist:
#         return redirect('main')
#     return render(request, 'app_headphones/detail.html', context={'headphone': headphone})