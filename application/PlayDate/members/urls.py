from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('aboutus/', views.about, name='about'),
#     path('soujanya/', views.soujanya, name='soujanya'),
#     path('qing/', views.qing, name='qing'),
# ]

urlpatterns = [
    #path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/soujanya/', views.soujanya, name='soujanya'),
    path('about/andy/', views.andy, name='andy'),
    path('about/margaret/', views.margaret, name='margaret'),
    path('about/martin/', views.martin, name='martin'),
    path('about/qin/', views.qin, name='qin'),
    path('about/william/', views.william, name='william'),
    path('about/victor/', views.victor, name='victor'),
]
