from django.urls import path
from .views import PostCreate, CategoryCreate, PostList, PostDetail, PostUpdate, PostDelete

urlpatterns = [
    path("category/new/", CategoryCreate.as_view(), name="category-created"),
    path("post/new/", PostCreate.as_view(), name="blog-created"),
    path("post/list/", PostList.as_view(), name="list-post"),
    path("post/<int:pk>/", PostDetail.as_view(), name="detail-post"),
    path("post/update/<int:pk>/", PostUpdate.as_view(), name="update-post"),
    path("post/delete/<int:pk>/", PostDelete.as_view(), name="delete-post")
]

