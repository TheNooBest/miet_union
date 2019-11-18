from django.conf.urls import handler400, handler403, handler404, handler500 # noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from .views import (
    commissions,
    help_proforg,
    home,
    login_view,
    logout_view,
    money_help,
    my_account,
    news_page,
    normative_document,
    our_team,
    personal_data_protection,
    profcom,
    profsouz,
    social_card,
    test_404,
    useful_links,
)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('admin_tools/', include('admin_tools.urls')),
    path('commissions', commissions, name='commissions'),
    path('favicon.ico', RedirectView.as_view(
        url='/static/images/favicon.ico')),
    path('helpproforg', help_proforg, name='helpproforg'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('moneyhelp', money_help, name='moneyhelp'),
    path('my_account', my_account, name='my_account'),
    path('news/<int:pk>', news_page, name='news_page'),
    path('normativedocument', normative_document, name='normativedocument'),
    path('ourteam', our_team, name='ourteam'),
    path('personaldataprotection', personal_data_protection,
         name='personaldataprotection'),
    path('profcom', profcom, name='profcom'),
    path('profsouz', profsouz, name='profsouz'),
    path('socialcard', social_card, name='socialcard'),
    path('summernote/', include('django_summernote.urls')),
    path('test', test_404, name='test'),
    path('usefullinks', useful_links, name='usefullinks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler400 = 'miet_union.views.error_400'
handler403 = 'miet_union.views.error_403'
handler404 = 'miet_union.views.error_404'
handler500 = 'miet_union.views.error_500'
