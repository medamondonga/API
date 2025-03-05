from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView
from django.shortcuts import render
from rest_framework.response import Response

from .models import Category, Post
from .serializers import CategoySerializer, PostSerializer

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
