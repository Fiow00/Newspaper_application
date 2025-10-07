from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from newspaper.models import Article
from .serializers import UserSerializer, ArticleSerializer


@api_view(["GET"])
def user_list(request):
    """Return a list of all users."""
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def article_list(request):
    """
    GET: Return a list of all articles.
    POST: Create a new article.
    """
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, pk):
    """
    GET: Retrieve a specific article.
    PUT: Update an article.
    DELETE: Delete an article.
    """
    article = get_object_or_404(Article, pk=pk)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
