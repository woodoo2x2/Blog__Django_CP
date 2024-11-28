from django.urls import path

from blog import views



urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/comments/create/', views.CommentCreateView.as_view(), name='comment_create_view'),
    path('category/<slug:slug>/', views.PostFromCategory.as_view(), name="post_by_category"),
    path("api/<int:pk>/", PostDetail.as_view(), name="post_detail_api"),
    path("api/", PostList.as_view(), name="post_list_api"),
]