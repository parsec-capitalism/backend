from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MissionViewSet, PlayerMissionLogViewSet, APIStartMission

router = DefaultRouter()
router.register('missions', MissionViewSet)
router.register('log', PlayerMissionLogViewSet, basename='mission-log')

app_name = 'missions'

urlpatterns = [
    path('', include(router.urls)),
    path('start_mission/', APIStartMission.as_view()),
]
