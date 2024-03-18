import django_filters
from .models import Article
from django import forms

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateFilter(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Article
        fields = ['title', 'category', 'date']
