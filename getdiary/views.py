from django.shortcuts import render


def home(request):
    return render(request, 'getdiary/home.html')


def test(request):
    return render(request, 'getdiary/test.html')
