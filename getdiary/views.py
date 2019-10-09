from django.shortcuts import render


def home(request):
    context = {'name': 'Птачек'}
    return render(request, 'getdiary/home.html', context)


def test(request):
    return render(request, 'getdiary/test.html')
