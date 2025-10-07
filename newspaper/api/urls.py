from django.urls import path

from . import views

# API endpoints for the newspaper app
urlpatterns = [
    path("users/", views.user_list, name="newspaper_user_list"),
    path("articles/", views.article_list, name="newspaper_article_list"),
    path("articles/<int:pk>/", views.article_detail, name="newspaper_article_detail"),
]
