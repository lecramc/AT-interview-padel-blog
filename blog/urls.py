from django.urls import path

from blog import views

urlpatterns = [
    path('', views.flux_view, name='flux'),
    path('articles/<int:pk>/', views.article_detail_view, name='article_detail'),
]