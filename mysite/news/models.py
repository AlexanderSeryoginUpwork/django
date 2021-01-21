from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')  # black=True т.е. необязательное поле
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # auto_now_add только один раз в момент создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')  # auto_now обновляет при каждом сохранении
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Фото', blank=True)  # python -m pip install Pillow
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    '''
    В админке при редактировании или создании нового поста, изображение является обязетельным.
    Чтоб сделать его не обязательным. нужно прописать black=True и перезапустить миграцию 
    python manage.py makemigrations && python manage.py migrate
    '''

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


def __str__(self):
    return self.title
