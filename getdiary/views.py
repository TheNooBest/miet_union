from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    context = {'name': 'Провком'}
    return render(request, 'base.html', context)
