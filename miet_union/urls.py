from django.contrib import admin
from django.urls import path

from .views import (
    home,
    ourteam,
    test,
    moneyhelp,
    socialcard,
    helpproforg,
    profcom,
    profsouz,
    commissions,
    normativedocument,
    personaldataprotection,
    usefullinks,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ourteam', ourteam, name='ourteam'),
    path('test', test, name='test'),
    path('moneyhelp', moneyhelp, name='moneyhelp'),
    path('socialcard', socialcard, name='socialcard'),
    path('helpproforg', helpproforg, name='helpproforg'),
    path('profcom', profcom, name='profcom'),
    path('profsouz', profsouz, name='profsouz'),
    path('commissions', commissions, name='commissions'),
    path('normativedocument', normativedocument, name='normativedocument'),
    path('personaldataprotection', personaldataprotection,
         name='personaldataprotection'),
    path('usefullinks', usefullinks, name='usefullinks'),
]
