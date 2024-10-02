from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from contact.forms import ContactForm


@login_required
def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'success': success})