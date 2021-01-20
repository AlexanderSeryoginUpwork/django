from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # black=True т.е. необязательное поле
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add только один раз в момент создания
    updated_at = models.DateTimeField(auto_now=True)  # auto_now обновляет при каждом сохранении
    photo = models.ImageField(upload_to='photos/%y/%m/%d')  # python -m pip install Pillow
    is_published = models.BooleanField(default=True)
