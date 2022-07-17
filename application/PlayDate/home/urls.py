from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registrationPage, name='register'),
    path('profileEdit/', views.profileEditPage, name='profileEdit'),
    path('profile/', views.profilePage, name='profile'),
    path('profile/<int:profile_id>/', views.profileView, name='profileView'),
    path('helpPage/', views.helpPage, name='helpPage'),
    path('termsofuse/', views.termsofuse, name='termsofuse'),
    path('privacy/', views.privacy, name='privacy'),
    path('comeSoon/', views.comesoonPage, name='comesoon'),
    path('support/', views.contactSupport, name='contactSupport'),
    path('myGroupsPage/', views.myGroupsPage, name='myGroupsPage'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]
