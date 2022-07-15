from django.urls import path

from . import views

urlpatterns = [
    path('', views.groups, name='groups'),
    path('createGroup/', views.createGroup, name='createGroup'),
    path('<int:group_id>/', views.groupView, name='groupView'),
    path('joinSuccess/', views.joinSuccess, name='joinSuccess'),
]
