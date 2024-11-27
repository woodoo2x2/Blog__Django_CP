


from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.views.generic import CreateView
from .forms import PostCreateForm


class PostCreateView(CreateView):
    """
    Представление: создание материалов на сайте
    """
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи на сайт'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostFromCategory(ListView):
    """Отображение статей по категориям"""
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    category = None
    paginate_by = 5

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.custom.filter(category__slug=self.category.slug)
        if not queryset:
            sub_cat = Category.objects.filter(parent=self.category)
            queryset = Post.custom.filter(category__in=sub_cat)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Записи из категории: {self.category.title}'
        return context


class PostListView(ListView):
    """Представление главной страницы"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.custom.all()

    def get_context_data(self, **kwargs):
        """Изменили в передаваемые значения"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная Страница'
        return context


class PostDetailView(DetailView):
    """Представление конкретной записи"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context