from django.test import TestCase

from django.urls import reverse

# Create your tests here.
class NewspaperTests(TestCase):
    def test_url_exists_at_correct_location_articlelistview(self):
        response = self.client.get("/newspaper/")
        self.assertEqual(response.status_code, 200)

    def test_articlelist_view(self):
        response = self.client.get(reverse("newspaper:article_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/article_list.html")
        self.assertContains(response, "Articles")