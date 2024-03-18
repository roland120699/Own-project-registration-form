from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    category = models.CharField(max_length=100, default=timezone.now)


    def __str__(self):
        return self.title