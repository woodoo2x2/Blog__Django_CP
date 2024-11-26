from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    """Представление главной страницы"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        """Изменили в передаваемые значения"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context