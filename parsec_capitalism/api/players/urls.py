from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PlayerViewSet

router = DefaultRouter()
router.register('players', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
