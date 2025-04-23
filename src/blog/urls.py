from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    )
from .views import PostCreate, CategoryCreate, PostList, PostDetail, PostUpdate, PostDelete

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="refresh"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("verify/", TokenVerifyView.as_view(), name="verify"),
    path("category/new/", CategoryCreate.as_view(), name="category-created"),
    path("post/new/", PostCreate.as_view(), name="blog-created"),
    path("post/list/", PostList.as_view(), name="list-post"),
    path("post/<int:pk>/", PostDetail.as_view(), name="detail-post"),
    path("post/update/<int:pk>/", PostUpdate.as_view(), name="update-post"),
    path("post/delete/<int:pk>/", PostDelete.as_view(), name="delete-post"),
]

