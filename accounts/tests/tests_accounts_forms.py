from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserUpdateForm, ProfileUpdateForm
from accounts.models import Profile


class TestUserUpdateForm(TestCase):

    def setUp(self):
        # Создаем пользователя для тестирования формы
        self.user = User.objects.create_user(username='testuser', password='password123')



    def test_user_update_form_invalid(self):
        """Тест на обновление формы (неправильная 'username' = '')"""
        data = {
            'username': '',
            'email': 'invalidemail'
        }
        form = UserUpdateForm(data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)

    def test_user_update_form_unique_username(self):
        """Тест на проверку уникальности username и выход в ошибку"""
        User.objects.create_user(username='anotheruser', password='password123')
        data = {
            'username': 'anotheruser',  # Используем уже существующий username
            'email': 'newemail@example.com'
        }
        form = UserUpdateForm(data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

class TestProfileUpdateForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile, created = Profile.objects.get_or_create(user=self.user, slug='testuser')


    def test_profile_update_form_invalid(self):
        data = {
            'bio': '',  # Пустое поле для необязательного поля 'bio'
            'birth_date': 'invalid-date',  # Неверный формат даты
            'avatar': None
        }
        form = ProfileUpdateForm(data, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('birth_date', form.errors)  # Ошибка на поле 'birth_date'

