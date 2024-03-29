from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__reload__/', include('django_browser_reload.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.customAuth.urls')),
    path("tasks/", include('apps.tasks.urls')),
    path('', include('apps.main.urls'))
]
