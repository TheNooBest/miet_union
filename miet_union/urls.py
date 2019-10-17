from django.contrib import admin
from django.urls import path

from .views import (
    home,
    ourteam,
    test,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ourteam', ourteam, name='ourteam'),
    path('test', test, name='test'),
]