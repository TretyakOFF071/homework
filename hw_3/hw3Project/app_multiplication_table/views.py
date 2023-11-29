from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def multiplication_table(request, *args, **kwargs):
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i*j)
        table.append(row)
    context = {'table': table}
    return render(request, 'app_multiplication_table/index.html', context=context)
