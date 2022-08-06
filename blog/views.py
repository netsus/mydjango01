from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "blog/index.html", context={"post_list": qs})


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)  # 해당 오브젝트가 없으면 404페이지로 보낸다.
    return render(request, "blog/post_detail.html", {"post": post})
