from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registrationPage, name='register'),
    path('public/', views.publicPage, name='public'),
    path('helpPage/', views.helpPage, name='helpPage'),
    path('termsofuse/', views.termsofuse, name='termsofuse'),
 ]
