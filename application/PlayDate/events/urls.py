from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('/public-events/', views.publicevents, name='publicevents'),
    #path('/members-events/', views.membersevents, name='membersevents'),
    # path('/my-events/', views.myevents, name='myevents'),
    # path('/my-events/createvent/', views.createGroupEvent, name='createGroupEvent'),
    path('filter', views.filter, name='filter'),
    path('/create_events/', views.createEvent, name='createEvent'),
]
