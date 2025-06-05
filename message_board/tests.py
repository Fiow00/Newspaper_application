from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/messages/")
        self.assertEqual(response.status_code, 200)

    def test_postspage(self):
        response = self.client.get(reverse("message_board:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "message_board/posts.html")
        self.assertContains(response, "This is a test!")
