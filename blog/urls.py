from django.urls import path

from blog import views

urlpatterns = [
    path('', views.flux_view, name='flux'),
    path('<int:pk>/', views.article_view, name='article'),
]