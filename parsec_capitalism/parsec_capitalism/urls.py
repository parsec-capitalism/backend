from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework.routers import DefaultRouter

from resources.views import ResourceViewSet
from ships.views import (
    ListUserShipViewSet,
    ListUserViewSet,
    ShipViewSet,
    UserShipViewSet,
)

router = DefaultRouter()
router.register("ships", ShipViewSet)
router.register("users", ListUserViewSet)
router.register("resources", ResourceViewSet)
router.register("users_ships", UserShipViewSet, basename="usership")
router.register(
    "list_users_ships", ListUserShipViewSet, basename="list_usership"
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
