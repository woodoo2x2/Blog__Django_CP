from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
from datetime import datetime
from django.urls import reverse


class PostTemplateTest(TestCase):
    def setUp(self):
        """Создаем пользователя, категорию и пост"""
        self.user = User.objects.create(username="testuser", password="password123")


        self.category = Category.objects.create(
            title="Test Category",
            slug="test-category",
            description="Description of test category"
        )


        self.post = Post.objects.create(
            title="Test Post",
            description="Short description of the test post",
            text="This is the full content of the test post",
            status="published",
            author=self.user,
            category=self.category,
        )

    def test_post_template_renders_correct_data(self):
        """Проверяем успешность запроса, выбор шаблона и данные передаваемые в шаблон"""
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.post.slug}))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/post_detail.html")

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.category.title)

