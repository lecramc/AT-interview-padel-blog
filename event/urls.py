from django.urls import path

from event import views

urlpatterns = [
    path('', views.events_list_view, name='events'),
]