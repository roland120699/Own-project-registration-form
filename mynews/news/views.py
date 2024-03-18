from django.shortcuts import render, get_object_or_404
from .filters import NewsFilter
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from allauth.account.views import SignupView
from .forms import CustomSignupForm

def news_list(request):
    news_list = Article.objects.all().order_by('pub_date', 'id')
    news_filter = NewsFilter(request.GET, queryset=news_list)

    paginator = Paginator(news_list, 10)
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/news_list.html', {'filter': news_filter, 'news': news})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news/article.detail.html', {'article': article})

class NewsCreateView(CreateView):
    model = Article
    template_name = 'news/news_form.html'
    fields = ['title', 'content', 'pub_date', 'category']
    success_url = reverse_lazy('news_list')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news/news_form.html'
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('news_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news_list')

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'news/article_form.html'
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('news_list')

def new_page_view(request):
    return render(request, 'news/news_page.html')

class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'registration/signup.html'
