from django.shortcuts import render

from .forms import RestaurantForm, SearchForm
from .models import Restaurant
from django.shortcuts import get_object_or_404, redirect

# Create your views here.


def restaurant_list(request):
    form = SearchForm(request.GET)

    if form.is_valid():
        specialization = form.cleaned_data.get('specialization')
        if specialization:
            restaurants = Restaurant.objects.filter(specialization__icontains=specialization)
            return render(request, 'app_restaurants/restaurant_filter.html',
                          context={'restaurants': restaurants, 'form': form})
    restaurants = Restaurant.objects.all()
    return render(request, 'app_restaurants/restaurant_list.html', context={'restaurants': restaurants, 'form': form})

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'app_restaurants/add_restaurant.html', context={'form': form})


def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'app_restaurants/restaurant_delete.html', context={'restaurant': restaurant})


def restaurant_edit(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'app_restaurants/restaurant_edit.html', context={'form': form})


