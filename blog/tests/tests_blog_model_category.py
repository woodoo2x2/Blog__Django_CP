from unittest import TestCase

from blog.models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        """Подготовка данных перед тестами: создание категории"""
        self.category = Category.objects.create(
            title="Test Category",
            slug="test-category",
            description="This is a test category",
        )

    def test_category_creation(self):
        """Тест создания категории"""
        self.assertEqual(self.category.title, "Test Category")
        self.assertEqual(self.category.slug, "test-category")
        self.assertEqual(self.category.description, "This is a test category")

    def test_category_absolute_url(self):
        """Тест правильности формирования URL"""
        self.assertEqual(
            self.category.get_absolute_url(),
            f"/category/{self.category.slug}/"
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")