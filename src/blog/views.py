from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView
from django.shortcuts import render
from rest_framework.response import Response

from .models import Category, Post
from .serializers import CategoySerializer, PostSerializer

"""Mixins for category"""


class CategoryCreate(CreateModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoySerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response(
                {
                    "message": "Categorie added successefuly"
                }
            )
        return response


"""Mixins for post"""


class PostCreate(CreateModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response(
                {
                    "message": "Article added successefuly"
                }
            )
        return response


class PostList(ListModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostDetail(RetrieveModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostUpdate(UpdateModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            return Response({
                "Message": "Article modifie avec success"
            }, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            return Response({
                "Message": "Article modifie avec success"
            }, status=status.HTTP_200_OK)

class PostDelete(DestroyModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs )

        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response({
                "Message": "Article supprime"
            }, status=status.HTTP_204_NO_CONTENT)