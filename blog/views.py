from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from blog.models import Article


@login_required
def flux_view(request):
    articles = Article.objects.all()
    return render(request, 'flux.html', {'articles': articles})

