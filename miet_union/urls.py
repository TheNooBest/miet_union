from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import (
    home,
    our_team,
    test,
    money_help,
    social_card,
    help_proforg,
    profcom,
    profsouz,
    commissions,
    normative_document,
    personal_data_protection,
    useful_links,
    login_view,
    logout_view,
    my_account
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ourteam', our_team, name='ourteam'),
    path('test', test, name='test'),
    path('moneyhelp', money_help, name='moneyhelp'),
    path('socialcard', social_card, name='socialcard'),
    path('helpproforg', help_proforg, name='helpproforg'),
    path('profcom', profcom, name='profcom'),
    path('profsouz', profsouz, name='profsouz'),
    path('commissions', commissions, name='commissions'),
    path('normativedocument', normative_document, name='normativedocument'),
    path('personaldataprotection', personal_data_protection,
         name='personaldataprotection'),
    path('usefullinks', useful_links, name='usefullinks'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('my_account', my_account, name='my_account'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
