from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserLoginForm


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

@login_required
def my_account(request):
    return render(request, 'miet_union/myaccount.html')


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next_ = request.GET.get('next')
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username.strip(),
                            password=password.strip())
        login(request, user)
        next_post = request.POST.get('next')
        rederict_path = next_ or next_post or '/'
        return redirect(rederict_path)
    return render(request, 'miet_union/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
