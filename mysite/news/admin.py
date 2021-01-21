from django.contrib import admin

# Register your models here.

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')  # какие поля отображать
    list_display_links = ('id', 'title')  # эти поля станут ссылкабельными
    search_fields = ('title', 'content')  # после добавления этого поля в админке появляется поле для поиска
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
