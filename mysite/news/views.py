from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class HomeNews(ListView):
    # c какой моделью работать, откуда брать данные
    model = News

    # какой шаблон будет использоваться вместо шаблона по-умолчанию
    template_name = 'news/home_news_list.html'

    # по какой переменной итерировать вместо object_list
    context_object_name = 'news'

    # дополнительные параметры страницы. Например, title
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    # отфильтрованные данные из БД
    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     return render(request, 'news/category.html', {'news': news, 'categories': categories})

class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    # при отсутствии категории показываем 404
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'

# def view_item2(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_item': news_item
#     }
#     return render(request, template_name='news/view_news.html', context=context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             print(
#                 form.cleaned_data)  # {'title': 'Новость из формы', 'content': 'Новость из формы 123', 'is_published': True, 'category': <Category: Наука>}
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#         else:
#             print('ololo')
#     else:
#         form = NewsForm()
#         pass
#
#     return render(request=request, template_name='news/add_news.html', context={'form': form})


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
