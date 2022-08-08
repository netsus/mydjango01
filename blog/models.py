from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.TextField()
