from django.shortcuts import render
from missions.models import Missions
from rest_framework import permissions, viewsets

from ships.serializers import ShipSerializer


# class ShipViewSet(viewsets.ModelViewSet):
#     queryset = Ships.objects.all()
#     serializer_class = ShipSerializer
#     permission_classes = [permissions.IsAuthenticated]


