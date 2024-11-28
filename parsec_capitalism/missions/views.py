from rest_framework import viewsets

from .models import Mission
from .serializers import MissionSerializer


class MissionViewSet(viewsets.ReadOnlyModelViewSet):
    """List of all Ships"""

    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
