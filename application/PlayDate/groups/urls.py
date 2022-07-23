# ░█░█░█▀▄░█░░
# ░█░█░█▀▄░█░░
# ░▀▀▀░▀░▀░▀▀▀
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Search, name='groups'),
    path('createGroup/', views.createGroup, name='createGroup'),
    path('<int:group_id>/', views.groupView, name='groupView'),
    path('search/', views.Search, name='groupSearch'),
    path('search/results/', views.searchResults, name='groupSearchResults'),
    path('joinSuccess/', views.joinSuccess, name='joinSuccess'),
    # For development use, this will be merged with the view Group page.
    path('testGroup/', views.testGroup, name="test"),
    # static: for prototype use
    path('individualGroup/', views.individualGroup, name='individualGroup'),
    # static: for prototype use
    path('myGroup/', views.myGroup, name='myGroup'),
]
