from django.shortcuts import render


def home(request):
    context = {'name': 'union_test'}
    return render(request, 'miet_union/home.html', context)


def our_team(request):
    context = {}
    return render(request, 'miet_union/ourteam.html', context)


def money_help(request):
    return render(request, 'miet_union/moneyhelp.html')


def test(request):
    return render(request, 'miet_union/test.html')


def social_card(request):
    return render(request, 'miet_union/socialcard.html')


def help_proforg(request):
    return render(request, 'miet_union/helpproforg.html')


def profcom(request):
    return render(request, 'miet_union/profcom.html')


def profsouz(request):
    return render(request, 'miet_union/profsouz.html')


def commissions(request):
    return render(request, 'miet_union/commissions.html')


def normative_document(request):
    return render(request, 'miet_union/normativedocument.html')


def personal_data_protection(request):
    return render(request, 'miet_union/personaldataprotection.html')


def useful_links(request):
    return render(request, 'miet_union/usefullinks.html')

