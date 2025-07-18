from django.test import TestCase

from django.contrib.auth import get_user_model

from django.urls import reverse

from .models import Article, Comment

# Create your tests here.
class NewspaperTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = get_user_model().objects.create_user(
            username = "testuser",
            email = "testuser@email.com",
            password = "testing321",
        )

        cls.article = Article.objects.create(
            title = "title",
            body = "body",
            author = cls.author,
        )

        cls.comment = Comment.objects.create(
            article = cls.article,
            comment = "comment",
            author = cls.author,
        )

    def test_user_model(self):
        self.assertEqual(self.author.username, "testuser")
        self.assertEqual(self.author.email, "testuser@email.com")

    def test_article_model(self):
        self.assertEqual(self.article.title, "title")
        self.assertEqual(self.article.body, "body")
        self.assertEqual(str(self.article), "title")

    def test_articlelist_view(self):
        self.client.login(username="testuser", password="testing321")
        response = self.client.get(reverse("newspaper:article_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/article_list.html")
        self.assertContains(response, "Articles")
        self.assertContains(response, self.article.title)
        self.assertContains(response, self.article.body)

    def test_articledetail_view(self):
        self.client.login(username="testuser", password="testing321")
        url = reverse("newspaper:article_detail", kwargs={"pk": self.article.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/article_detail.html")
        self.assertContains(response, self.article.title)
        self.assertContains(response, self.article.body)
        self.assertContains(response, "Comments")
        self.assertContains(response, "Add a comment")

    def test_articleedit_view(self):
        self.client.login(username="testuser", password="testing321")
        url = reverse("newspaper:article_edit", kwargs={"pk": self.article.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/article_edit.html")
        self.assertContains(response, "Edit")
        self.assertContains(response, "Update")

    def test_articledelete_view(self):
        self.client.login(username="testuser", password="testing321")
        url = reverse("newspaper:article_delete", kwargs={"pk": self.article.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/article_delete.html")
        self.assertContains(response, "Delete")
        self.assertContains(response, "Are you sure you want to delete")

    def test_articlenew_view(self):
        self.client.login(username="testuser", password="testing321")
        url = reverse("newspaper:article_new")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/article_new.html")
        self.assertContains(response, "New article")
        self.assertContains(response, "Save")
