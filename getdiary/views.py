from django.shortcuts import render


def home(request):
    context = {'name': '228_Potato_Freeman_228'}
    return render(request, 'getdiary/home.html', context)


def test(request):
    return render(request, 'getdiary/test.html')
