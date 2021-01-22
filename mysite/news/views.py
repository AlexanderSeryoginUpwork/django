from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

# Create your views here.


def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'My title',
        'categories': categories
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    context = {
        'news': news,
        'category': category,
        'categories': categories
    }
    return render(request=request, template_name='news/category.html', context=context)
