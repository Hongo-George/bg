from django.urls import path
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, BlogPostCategoryView
from .models import BlogPost

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
]
