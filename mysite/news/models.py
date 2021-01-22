from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')  # black=True т.е. необязательное поле
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # auto_now_add только один раз в момент создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')  # auto_now обновляет при каждом сохранении
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Фото', blank=True)  # python -m pip install Pillow
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    #  category доступна как внешний ключ
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=1, verbose_name='Категория')  #  models.PROTECT защищает связанные данные от удаления

    '''
    В админке при редактировании или создании нового поста, изображение является обязетельным.
    Чтоб сделать его не обязательным. нужно прописать black=True и перезапустить миграцию 
    python manage.py makemigrations && python manage.py migrate
    '''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=140, db_index=True, verbose_name='Наименование категории')

    '''
        без приведения к строке список категорий будет примерно таким:
        <Category Object(1)>
        <Category Object(2)>
        <Category Object(3)>
        <Category Object(4)>
    '''
    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']



