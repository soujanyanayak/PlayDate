from django.urls import path

from . import views

urlpatterns = [
    path('', views.Search, name='groups'),
    path('createGroup/', views.createGroup, name='createGroup'),
    path('<int:group_id>/', views.groupView, name='groupView'),
    path('search/', views.Search, name='groupSearch'),
    path('search/results/', views.searchResults, name='groupSearchResults'),
    path('joinSuccess/', views.joinSuccess, name='joinSuccess'),
]
