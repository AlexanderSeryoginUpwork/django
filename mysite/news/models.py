from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    # black=True т.е. необязательное поле
    content = models.TextField(blank=True)
    # auto_now_add только один раз в момент создания
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now обновляет при каждом сохранении
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    is_published = models.BooleanField(default=True)
