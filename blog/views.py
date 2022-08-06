from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "blog/index.html", context={"post_list": qs})
