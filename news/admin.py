from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model = News
    list_display = ('title',
                    'main_text',
                    'image',
                    )
    list_filter = ('title', 'main_text')

admin.site.register(News, NewsAdmin)
