from django.shortcuts import render
from ships.models import Ships
from rest_framework import permissions, viewsets

from ships.serializers import ShipSerializer


class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ships.objects.all()
    serializer_class = ShipSerializer
    permission_classes = [permissions.IsAuthenticated]


def ships_list(request):
    template = 'ships/ships.html'
    ships_list = Ships.objects.all()
    context = {
        'ships_list': ships_list,
    }
    return render(request, template, context)
