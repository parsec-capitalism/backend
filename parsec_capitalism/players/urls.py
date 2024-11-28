from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PlayerViewSet

router = DefaultRouter()
router.register('players', PlayerViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
