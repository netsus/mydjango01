from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    def get_abolute_url(self):
        return reverse("blog:post_detail")


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
