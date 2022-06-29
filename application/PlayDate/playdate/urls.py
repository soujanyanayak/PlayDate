from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('groups', include('groups.urls')),
    #    path('about/', include('members.urls')),
]

# Use static() to add URL mapping to serve static files during development (only)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
