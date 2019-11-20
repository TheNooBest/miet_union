from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.conf.urls import handler400, handler403, handler404, handler500 # noqa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm

from .forms import UserLoginForm
from news.models import News
from ourteam.models import Worker


def home(request):
    news = News.objects.all()
    reversed_news = []
    for i in reversed(news):
        reversed_news.append(i)

    paginator = Paginator(news, 5)

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {
        'news': news,
        'reversed_news': reversed_news,
        }

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

    context.update({'form': form})
    return render(request, 'miet_union/home.html', context)


def our_team(request):
    worker = Worker.objects.all()
    context = {
        'worker': worker,
        }
    return render(request, 'miet_union/ourteam.html', context)


def registration_view(request):
    form = UserCreationForm(data=request.POST or None)
    next_ = request.GET.get('next')
    if request.method == 'POST' and form.is_valid():
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or '/'
        form.save()
        return redirect('/login')

    return render(request, "miet_union/registration.html", { 'form': form})


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


@login_required
def my_account(request):
    return render(request, 'miet_union/myaccount.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def news_page(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'miet_union/news_page.html', {'news': news})


def error_400(request, exception):
    return render(request, 'miet_union/400.html')


def error_403(request, exception):
    return render(request, 'miet_union/403.html')


def error_404(request, exception):
    return render(request, 'miet_union/404.html')


def error_500(request):
    return render(request, 'miet_union/500.html')


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


def test_404(request):
    return render(request, 'miet_union/404.html')


def commissions(request):
    return render(request, 'miet_union/commissions.html')


def normative_document(request):
    return render(request, 'miet_union/normativedocument.html')


def personal_data_protection(request):
    return render(request, 'miet_union/personaldataprotection.html')


def useful_links(request):
    return render(request, 'miet_union/usefullinks.html')
