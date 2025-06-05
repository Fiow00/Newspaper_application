from django.urls import path

from . import views

app_name = "message_board"

urlpatterns = [
    path("", views.Posts.as_view(), name="post_list"),
]
