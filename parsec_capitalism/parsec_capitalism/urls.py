from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from ships.views import ShipViewSet, UserViewSet, UserShipViewSet

router = DefaultRouter()
router.register('ships', ShipViewSet)
router.register('users', UserViewSet)
router.register('users_ships', UserShipViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
