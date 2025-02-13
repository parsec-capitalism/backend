from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APIBuyShip,
    ListUserShipViewSet,
    ShipViewSet,
)

router = DefaultRouter()
router.register('ships', ShipViewSet)
router.register(
    'hangar',
    ListUserShipViewSet,
    basename='hangar',
)


urlpatterns = [
    path('', include(router.urls)),
    path('buy_ship/', APIBuyShip.as_view()),
]
