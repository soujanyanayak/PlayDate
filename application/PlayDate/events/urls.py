from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('createEvent/', views.createEvent, name='eventCreate'),
    path('filter/', views.filter, name='filter'),
]
