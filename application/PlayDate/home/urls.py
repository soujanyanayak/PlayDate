from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registrationPage, name='register'),
    path('individuleInfo/', views.individuleInfoPage, name='individuleInfo'),
    path('helpPage/', views.helpPage, name='helpPage'),
    path('termsofuse/', views.termsofuse, name='termsofuse'),
    path('privacy/', views.privacy, name='privacy'),
 ]
