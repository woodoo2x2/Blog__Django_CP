from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import ProfileDetailView, ProfileUpdateView

class TestProfileUrls(SimpleTestCase):
    """Тест для проверки URL"""
    def test_profile_detail_url(self):
        url = reverse('profile_detail', kwargs={'slug': 'test-user'})
        self.assertEqual(resolve(url).func.view_class, ProfileDetailView)

    def test_profile_edit_url(self):
        url = reverse('profile_edit')
        self.assertEqual(resolve(url).func.view_class, ProfileUpdateView)