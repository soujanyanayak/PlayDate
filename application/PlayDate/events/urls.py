from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('/public-events/', views.publicevents, name='publicevents'),
    path('/my-events/', views.myevents, name='myevents'),
    path('/my-events/create-user-event/', views.createUserEvent, name='createUserEvent'),
    path('filter', views.filter, name='filter'),
    path('/createEvent/', views.createEvent, name='createEvent'),
    path('/publicEvent1/', views.publicEvent1, name='publicEvent1'),
    path('/memberEvent1/', views.memberEvent1, name='memberEvent1'),
    path('/signUpSucceed/', views.signUpSucceed, name='signUpSucceed'),
    path('/my-events/', views.myEvent, name='myEvent'),
]
