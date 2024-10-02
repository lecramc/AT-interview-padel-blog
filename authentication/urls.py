from django.contrib.auth import views as auth

from django.urls import path

from authentication.views import register_view

urlpatterns = [
    path("login/", auth.LoginView.as_view(template_name="login.html"), name="login"),
    path('register/', register_view, name='register'),
]