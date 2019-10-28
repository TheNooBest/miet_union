from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    main_text = models.CharField(max_length = 2000, verbose_name='Текст новости')
    image = models.FileField(
        upload_to="media/news/images", verbose_name='Изображение')
    created = models.DateField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']