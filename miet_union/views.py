from django.shortcuts import render


def home(request):
    context = {'name': 'union_test'}
    return render(request, 'miet_union/home.html', context)


def ourteam(request):
    context = {}
    return render(request, 'miet_union/ourteam.html', context)


def moneyhelp(request):
    return render(request, 'miet_union/moneyhelp.html')


def test(request):
    return render(request, 'miet_union/test.html')


def socialcard(request):
    return render(request, 'miet_union/socialcard.html')


def helpproforg(request):
    return render(request, 'miet_union/helpproforg.html')


def profcom(request):
    return render(request, 'miet_union/profcom.html')


def profsouz(request):
    return render(request, 'miet_union/profsouz.html')


def commissions(request):
    return render(request, 'miet_union/commissions.html')


def normativedocument(request):
    return render(request, 'miet_union/normativedocument.html')


def personaldataprotection(request):
    return render(request, 'miet_union/personaldataprotection.html')


def usefullinks(request):
    return render(request, 'miet_union/usefullinks.html')
