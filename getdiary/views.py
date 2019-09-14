from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    context = {'name': 'Artem'}
    return render(request, 'base.html', context)

def home_view1(request):
    context = {'name': 'Artem'}
    return render(request, 'base.html', context)
