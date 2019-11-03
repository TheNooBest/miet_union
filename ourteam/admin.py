from django.contrib import admin
from .models import Worker


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


admin.site.register(Worker, WorkerAdmin)
