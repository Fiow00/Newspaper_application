from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    """Model representing an article published by a user."""
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("newspaper:article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    """Model representing a comment made on an article."""
    
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("newspaper:article_detail", kwargs={"pk": self.article.pk})
