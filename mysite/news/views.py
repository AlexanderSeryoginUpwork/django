from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'news/category.html', {'news': news, 'categories': categories})


def view_item2(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item
    }
    return render(request, template_name='news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
        pass

    return render(request=request, template_name='news/add_news.html', context={'form': form})
