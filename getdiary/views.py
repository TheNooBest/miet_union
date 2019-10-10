from django.shortcuts import render


def home(request):
    context = {'name': 'union_test'}
    return render(request, 'getdiary/home.html', context)


def test(request):
    return render(request, 'getdiary/test.html')
