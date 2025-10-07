from rest_framework import serializers

from django.contrib.auth import get_user_model

from newspaper.models import Article, Comment


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "is_superuser")


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""
    
    class Meta:
        model = Comment
        fields = ("comment",)


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for the Article model with nested author and comments."""
    
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ("title", "body", "date", "author", "comments")
