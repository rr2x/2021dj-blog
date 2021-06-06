from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # redirect after posting form
        # reverse = use the url name to calculate path and execute
        # reverse_lazy = if we are returning a value where to reverse and executed later
        return reverse("post_detail", args=[str(self.id)])
