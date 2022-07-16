from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('/public-events/', views.publicevents, name='publicevents'),
    path('/my-events/', views.myevents, name='myevents'),
    path('/my-events/create-user-event/', views.createUserEvent, name='createUserEvent'),
    path('filter', views.filter, name='filter'),
]
