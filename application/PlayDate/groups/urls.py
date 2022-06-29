from django.urls import path

from . import views

urlpatterns = [
    path('groups/', views.groups, name='groups'),
    path('createGroup/', views.createGroup, name='createGroup'),
]
