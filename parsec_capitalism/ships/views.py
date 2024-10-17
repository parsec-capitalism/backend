from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Ship, User, UserShip
from .serializers import ShipSerializer, UserSerializer, UserShipSerializer
from resources.models import Resource


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserShipViewSet(viewsets.ModelViewSet):
    queryset = UserShip.objects.all()
    serializer_class = UserShipSerializer

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, username=pk)
        queryset = UserShip.objects.filter(user=user)
        usership = get_list_or_404(queryset)
        serializer = UserShipSerializer(usership, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        ship = self.request.data.get('ship')
        ship = get_object_or_404(Ship, slug=ship)
        ship_cost = ship.cost 

        user_resource = get_object_or_404(Resource, user=self.request.user)
        user_resource.datacoin -= ship_cost
        user_resource.save()

        serializer.save(user=self.request.user)
