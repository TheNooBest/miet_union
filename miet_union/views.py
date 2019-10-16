from django.shortcuts import render


def home(request):
    context = {'name': 'union_test'}
    return render(request, 'miet_union/home.html', context)


def test(request):
    return render(request, 'miet_union/test.html')
