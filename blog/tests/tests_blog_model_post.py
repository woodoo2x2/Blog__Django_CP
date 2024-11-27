from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Category


class PostModelTest(TestCase):

    def setUp(self):
        """Подготовка данных перед тестами: создание пользователя,
        категории и поста."""

        self.user = User.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(title='C++',
                                                slug='cpp',
                                                description='C++')
        self.post = Post.objects.create(
            title='C++ discussing',
            description='Steve Klabnik and Herb Sutter Talk about Rust and C++',
            text='test_text',
            status='published',
            author=self.user,
            category=self.category
        )

    def test_create_post(self):
        """Тест на создание поста"""
        self.assertIsInstance(self.post, Post)
        self.assertEqual(self.post.title, 'C++ discussing')
        self.assertEqual(self.post.description, 'Steve Klabnik and Herb Sutter Talk about Rust and C++')
        self.assertEqual(self.post.text,
                         'test_text')
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.category.title, "C++")

    def test_post_slug_generation(self):
        """Тест на генерацию слага"""
        post = Post.objects.create(
            title="Another Post",
            description="Description of the post",
            text="Content of the post",
            author=self.user,
            category=self.category
        )
        self.assertTrue(post.slug)

    def test_get_absolute_url(self):
        """Проверяем правильность работы метода get_absolute_url"""
        expected_url = reverse('post_detail', kwargs={'slug': self.post.slug})
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_post_manager_published(self):
        """Создаем еще один пост со статусом draft и проверим
        что кастомный менеджер возвращает только опубликованные записи"""

        Post.objects.create(
            title="Draft Post",
            description="Description of draft post",
            text="Content of draft post",
            author=self.user,
            category=self.category,
            status="draft"
        )
        published_posts = Post.custom.all()
        self.assertEqual(published_posts.count(), 1)
        self.assertEqual(published_posts[0], self.post)

    def test_create_post_with_thumbnail(self):
        """Тест создания поста с изображением"""

        post = Post.objects.create(
            title="Post with Image",
            description="Test description",
            text="Full post text",
            status="published",
            author=self.user,
            category=self.category,
            thumbnail='../media/images/avatars/test_image.png'
        )
        self.assertTrue(post.thumbnail)
