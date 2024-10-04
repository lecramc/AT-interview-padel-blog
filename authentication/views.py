from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


from authentication.forms import RegisterForm


# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("login")