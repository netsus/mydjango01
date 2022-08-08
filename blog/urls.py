from django.urls import path
from . import views as blog_views

app_name = "blog"

urlpatterns = [
    path("", blog_views.index, name="index"),
    path("<int:pk>/", blog_views.post_detail, name="post_detail"),
    path("new/", blog_views.post_new, name="post_new"),
]
