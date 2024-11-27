from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from accounts.forms import UserUpdateForm
from accounts.models import Profile

class TestProfileUpdateView(TestCase):
    def setUp(self):
        """Первичная настройка"""
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Если профиль еще не существует, создаем его
        self.profile, created = Profile.objects.get_or_create(user=self.user, slug='testuser')

    def test_profile_update_view_status_code(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)

    def test_profile_update_view_template(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile_edit'))
        self.assertTemplateUsed(response, 'accounts/profile_edit.html')

    def test_profile_update_view_context(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile_edit'))
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], f'Редактирование профиля пользователя: {self.user.username}')
        self.assertIsInstance(response.context['user_form'], UserUpdateForm)


class TestProfileDetailView(TestCase):
    def setUp(self):
        """Первичная настройка"""
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Если профиль еще не существует, создаем его
        self.profile, created = Profile.objects.get_or_create(user=self.user, slug='testuser')

    def test_profile_detail_view_status_code(self):
        """Тест статус кода при входе"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile_detail', kwargs={'slug': 'testuser'}))
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_view_template(self):
        """Тест шаблона отображаемого при входе"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile_detail', kwargs={'slug': 'testuser'}))
        self.assertTemplateUsed(response, 'accounts/profile_detail.html')

    def test_profile_detail_view_context(self):
        """Тест передачи данных"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile_detail', kwargs={'slug': 'testuser'}))
        self.assertEqual(response.context['profile'], self.profile)
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], f'Профиль пользователя: {self.user.username}')