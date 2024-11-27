from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Category
from datetime import datetime


class PostListViewTest(TestCase):
    """Тесты для представления главной страницы"""

    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password123")
        self.category = Category.objects.create(title="Test Category", slug="test-category", description="Description")
        for i in range(6):
            Post.objects.create(
                title=f"Post {i + 1}",
                description=f"Description {i + 1}",
                text=f"Text content {i + 1}",
                status="published",
                author=self.user,
                category=self.category,
            )

    def test_post_list_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_list_view_pagination(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['posts']), 5)

    def test_post_list_view_context(self):
        response = self.client.get(reverse('home'))
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], 'Главная Страница')


class PostFromCategoryViewTest(TestCase):
    """Тесты для представления статей по категориям"""

    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password123")
        self.parent_category = Category.objects.create(title="Parent Category", slug="parent-category", description="Parent Description")
        self.sub_category = Category.objects.create(title="Sub Category", slug="sub-category", description="Sub Description", parent=self.parent_category)
        Post.objects.create(
            title="Parent Post",
            description="Description",
            text="Parent category post content",
            status="published",
            author=self.user,
            category=self.parent_category,
        )
        Post.objects.create(
            title="Subcategory Post",
            description="Description",
            text="Subcategory post content",
            status="published",
            author=self.user,
            category=self.sub_category,
        )

    def test_post_from_category_view_status_code(self):
        response = self.client.get(reverse('post_by_category', kwargs={'slug': self.parent_category.slug}))
        self.assertEqual(response.status_code, 200)

    def test_post_from_category_view_correct_template(self):
        response = self.client.get(reverse('post_by_category', kwargs={'slug': self.parent_category.slug}))
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_from_category_view_context(self):
        response = self.client.get(reverse('post_by_category', kwargs={'slug': self.parent_category.slug}))
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], f'Записи из категории: {self.parent_category.title}')



class PostDetailViewTest(TestCase):
    """Тесты для представления конкретной записи"""

    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password123")
        self.category = Category.objects.create(title="Test Category", slug="test-category", description="Description")
        self.post = Post.objects.create(
            title="Test Post",
            description="Short description",
            text="Full post content",
            status="published",
            author=self.user,
            category=self.category,
        )

    def test_post_detail_view_status_code(self):
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_correct_template(self):
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.post.slug}))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_detail_view_context(self):
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.context['post'], self.post)
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], self.post.title)