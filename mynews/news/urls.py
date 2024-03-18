from django.urls import path, include
from django.contrib import admin
from .views import news_list, article_detail, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, new_page_view
from .views import CustomSignupView

urlpatterns = [
    path('', news_list, name='news_list'),
    path('<int:article_id>/', article_detail, name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='news_create'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('news/edit/<int:pk>/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('signup', CustomSignupView.as_view(), name='custom_signup')
]
