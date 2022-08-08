from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import CreateView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html")),
    path("logout/", LogoutView.as_view(next_page="/blog/")),
    path(
        "signup/",
        CreateView.as_view(
            form_class=UserCreationForm,
            template_name="accounts/signup.html",
            success_url=settings.LOGIN_URL,
        ),
    ),
]
