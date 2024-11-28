from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(unique=True, max_length=255)
    body = models.TextField(unique=True, max_length=10_000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
