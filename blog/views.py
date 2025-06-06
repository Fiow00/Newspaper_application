from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blog/posts.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:post_list")
