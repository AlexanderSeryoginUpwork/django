from django.contrib import admin

# Register your models here.

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')  # какие поля отображать
    list_display_links = ('id', 'title')  # эти поля станут ссылкабельными
    search_fields = ('title', 'content')  # после добавления этого поля в админке появляется поле для поиска


admin.site.register(News, NewsAdmin)
