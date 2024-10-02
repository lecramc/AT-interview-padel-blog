from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect('flux')  # Remplace 'flux' par le nom de ta vue ou URL de flux
    return redirect('login')