from django.shortcuts import render


def home(request):
    context = {'name': 'union_test'}
    return render(request, 'miet_union/home.html', context)

def ourteam(request):
    context = {}
    return render(request, 'miet_union/ourteam.html', context)

def MoneyHelp(request):
    return render(request, 'miet_union/MoneyHelp.html')

def test(request):
    return render(request, 'miet_union/test.html')
