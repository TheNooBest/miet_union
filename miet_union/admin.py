from admin_tools.dashboard import Dashboard
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from news.models import News
from ourteam.models import Worker


class CustomDashboard(Dashboard):
    colomns = 3
    title = ('Profcom - admin console')

    def __init__(self, **kwargs):
        Dashboard.__init__(**kwargs)


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = 'main_text'
    fields = ['title', 'main_text', 'image', 'created']
    list_display = ('title',
                    'image',
                    'created',)
    list_filter = ('title', 'main_text', 'created')


class WorkerAdmin(admin.ModelAdmin):
    class Meta:
        model = Worker
    list_display = ('first_name',
                    'last_name',
                    'middle_name',
                    'position',
                    'phone_num',
                    'email',
                    'photo',
                    )
    list_filter = ('last_name', 'first_name')


admin.site.index_title = ('Профком')
admin.site.site_title = ('Административная консоль')

admin.site.register(Worker, WorkerAdmin)
admin.site.register(News, NewsAdmin)
