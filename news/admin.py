from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = 'title, main_text'
    fields = ['title', 'main_text', 'image', 'created']
    list_display = ('title',
                    'main_text',
                    'image',
                    'created',)
    list_filter = ('title', 'main_text', 'created')

admin.site.register(News, NewsAdmin)
