from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


from authentication.forms import RegisterForm


# Create your views here.
def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("login")