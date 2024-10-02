from django.shortcuts import render

from blog.models import Article


# Create your views here.
def flux(request):
    articles = Article.objects.all()
    return render(request, 'flux.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {'article': article})