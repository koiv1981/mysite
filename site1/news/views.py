# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class HomeCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


def get_context_data(self, *, object_list=None, **kwargs):
    context = super(HomeCategory, self).get_context_data(**kwargs)
    context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
    return context


def get_queryset(self):
    return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class AddNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')
    login_url = "/admin/"
