from rest_framework import serializers
from .models import Category, Post


class CategoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
