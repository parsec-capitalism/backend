from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APIBuyPerk,
    APIBuyShip,
    ListUserShipViewSet,
    PerkViewSet,
    ShipViewSet,
)

router = DefaultRouter()
router.register('ships', ShipViewSet)
router.register('perks', PerkViewSet)
router.register(
    'hangar',
    ListUserShipViewSet,
    basename='hangar',
)


urlpatterns = [
    path('', include(router.urls)),
    path('buy_ship/', APIBuyShip.as_view()),
    path('buy_perk/', APIBuyPerk.as_view()),
]
