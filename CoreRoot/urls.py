from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/auth/register', include(('core.routers', 'core'))), 
    path('api/', include(('core.routers', 'core'), namespace='core-api')), 
]
