# Register your models here.
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Админ-панель модели записей
    """
    prepopulated_fields = {'slug': ('title',)}

from .models import Comment

@admin.register(Comment)
class CommentAdminPage:
    """
    Админ-панель модели комментариев
    """
    pass