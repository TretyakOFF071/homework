from django.shortcuts import render
from .forms import NumberForm

def calculate(request):
    result = None
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            num3 = form.cleaned_data['num3']
            operation = form.cleaned_data['operation']

            if operation == 'min':
                result = min(num1, num2, num3)
            elif operation == 'max':
                result = max(num1, num2, num3)
            else:
                result = (num1 + num2 + num3) / 3
    else:
        form = NumberForm()

    return render(request, 'app_numbers/calculate.html', context={'form': form, 'result': result})