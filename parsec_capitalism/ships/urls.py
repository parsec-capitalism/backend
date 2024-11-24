from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ships.views import (
    ListUserShipViewSet,
    ListUserViewSet,
    ShipViewSet,
    UserShipViewSet,
)

router = DefaultRouter()
router.register('ships', ShipViewSet)
router.register('users', ListUserViewSet)
router.register('users_ships', UserShipViewSet, basename='usership')
router.register('list_users_ships', ListUserShipViewSet, basename='list_usership')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
