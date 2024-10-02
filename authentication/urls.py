from django.contrib.auth import views as auth

from django.urls import path

from authentication.views import RegisterView

urlpatterns = [
    path("login/", auth.LoginView.as_view(template_name="login.html"), name="login"),
    path('register/', RegisterView, name='register'),
]