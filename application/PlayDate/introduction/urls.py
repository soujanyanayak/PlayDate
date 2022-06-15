from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.about, name='about'),
    path('soujanya/', views.soujanya, name='soujanya'),
    path('qing/', views.qing, name='qing'),
]