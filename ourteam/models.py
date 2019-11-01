from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    position = models.CharField(max_length=100, verbose_name="Должность")
    phone_num = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')
    photo = models.ImageField(
        upload_to="workers/images", verbose_name='Фото')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ['last_name']
