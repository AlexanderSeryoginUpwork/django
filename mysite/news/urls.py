from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>', view_item2, name='view_item3'),
    path('news/add', add_news, name='add_news'),
]
