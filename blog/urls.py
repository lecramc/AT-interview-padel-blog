from django.urls import path

from blog import views

urlpatterns = [
    path('', views.flux, name='flux'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
]