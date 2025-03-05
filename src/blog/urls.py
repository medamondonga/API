from django.urls import path
from .views import PostCreate, CategoryCreate

urlpatterns = [
    path("category/new/", CategoryCreate.as_view(), name="category-created"),
    path("post/new/", PostCreate.as_view(), name="blog-created"),
]

