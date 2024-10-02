from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text="Requis. Veuillez entrer une adresse email valide.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')