from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from missions.models import Mission, PlayerMission
from .serializers import (
    MissionSerializer,
    PlayerMissionLogSerializer,
    StartMissionSerializer
)


class MissionViewSet(viewsets.ReadOnlyModelViewSet):
    """List of all Missions"""
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = (IsAuthenticated,)


class PlayerMissionLogViewSet(viewsets.ReadOnlyModelViewSet):
    """Player's mission history"""
    serializer_class = PlayerMissionLogSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PlayerMission.objects.filter(
            player=self.request.user
        ).select_related('mission', 'ship__ship')


class APIStartMission(APIView):
    """API for starting a mission. Request needs mission_id and ship_id."""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = StartMissionSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        
        mission = serializer.validated_data['mission']
        ship = serializer.validated_data['ship']
        
        # Create player mission
        player_mission = PlayerMission.objects.create(
            player=request.user,
            mission=mission,
            ship=ship,
            status=PlayerMission.MissionStatus.IN_PROGRESS
        )
        
        # Mark ship as on mission
        ship.on_mission = True
        ship.save()
        
        # Return the created mission
        return_serializer = PlayerMissionLogSerializer(player_mission)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)
