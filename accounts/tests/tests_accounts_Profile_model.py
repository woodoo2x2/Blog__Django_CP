from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Profile

class ProfileModelTest(TestCase):
    """Тесты для модели Profile"""

    def setUp(self):
        """Создаем тестового пользователя и профиль"""
        self.user = User.objects.create(username="testuser", password="password123")

        # Используем get_or_create для предотвращения дублирования
        self.profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                "bio": "This is a test bio.",
                "birth_date": "1990-01-01",
            },
        )

    def test_profile_creation(self):
        """Проверка создания профиля"""
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.avatar.name, "images/avatars/default.png")

    def test_profile_slug_generation(self):
        """Проверка генерации уникального slug"""
        self.assertEqual(self.profile.slug, "testuser")

    def test_profile_absolute_url(self):
        """Проверка метода get_absolute_url"""
        self.assertEqual(
            self.profile.get_absolute_url(),
            f"/user/{self.profile.slug}/",
        )

    def test_profile_str_method(self):
        """Проверка строкового представления профиля"""
        self.assertEqual(str(self.profile), "testuser")

    def test_profile_save_without_slug(self):
        """Проверка, что slug генерируется при сохранении, если он не задан"""
        new_user = User.objects.create(username="anotheruser", password="password123")
        profile, created = Profile.objects.get_or_create(
            user=new_user,
            defaults={
                "bio": "This is a test bio.",
                "birth_date": "1990-01-01",
            },
        )
        self.assertEqual(profile.slug, "anotheruser")

    def test_profile_save_with_custom_slug(self):
        """Проверка, что пользовательский slug сохраняется"""
        custom_slug = "custom-slug"
        self.profile.slug = custom_slug
        self.profile.save()
        self.assertEqual(self.profile.slug, custom_slug)