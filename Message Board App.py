"django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pages.apps.PagesConfig",  # new
]
from django.db import models


class Post(models.Model):
    text = models.TextField()

    def __str__(self):  # new
        return self.text[:50]

    from django.contrib import admin

    from .models import Post

    admin.site.register(Post)
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    < h1 > Message
    board
    homepage < / h1 >
    < ul >
    { %
    for post in post_list %}
    < li > {{post.text}} < / li >


{ % endfor %}
< / ul >
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
from django.test import TestCase
from django.urls import reverse  # new
from .models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):  # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")
ALLOWED_HOSTS = []"HerokuApp.com, "Local Host", 127.0.0.1"
