from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    MissionViewSet,
)

router = DefaultRouter()
router.register('missions', MissionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
