from django.shortcuts import render
from missions.models import Missions
from rest_framework import permissions, viewsets

from ships.serializers import ShipSerializer


# class ShipViewSet(viewsets.ModelViewSet):
#     queryset = Ships.objects.all()
#     serializer_class = ShipSerializer
#     permission_classes = [permissions.IsAuthenticated]


def missions_list(request):
    template = 'missions/missions.html'
    missions_list = Missions.objects.all()
    return render(request, template, {'missions_list': missions_list})
