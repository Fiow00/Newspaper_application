from django.contrib.auth import get_user_model

from rest_framework import serializers

from newspaper.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "is_superuser")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("comment",)

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ("title", "body", "date", "author", "comments")