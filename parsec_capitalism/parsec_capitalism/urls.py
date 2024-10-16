from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from ships.views import ShipViewSet, UserViewSet, UserShipViewSet
from resources.views import ResourceViewSet

router = DefaultRouter()
router.register('ships', ShipViewSet)
router.register('users', UserViewSet)
router.register('resources', ResourceViewSet)
router.register('users_ships', UserShipViewSet, basename='usership')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
