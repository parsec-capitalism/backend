from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework import routers

from ships import views

router = routers.DefaultRouter()
router.register(r'ships', views.ShipViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
