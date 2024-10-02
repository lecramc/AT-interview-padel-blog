from django.contrib.auth import login
from django.shortcuts import render, redirect


from authentication.forms import RegisterForm


# Create your views here.
def LoginView(request):
    return render(request, 'index.html')


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})