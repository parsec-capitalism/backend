from rest_framework import viewsets

from players.models import Player

from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
