from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Ship, User, UserShip
from .serializers import ShipSerializer, UserSerializer, UserShipSerializer


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    """List of Ships"""

    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class ListUserViewSet(viewsets.ReadOnlyModelViewSet):
    """List of Users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUserShipViewSet(viewsets.ModelViewSet):
    """List of Ships owned by logged in User"""

    def list(self, request):
        queryset = UserShip.objects.filter(user=request.user)
        serializer = UserShipSerializer(queryset, many=True)
        return Response(serializer.data)


class UserShipViewSet(viewsets.ModelViewSet):
    """Endpoint for buying a ship."""

    queryset = UserShip.objects.all()
    serializer_class = UserShipSerializer

    def perform_create(self, serializer):
        ship_slug = self.request.data.get('ship')
        ship = get_object_or_404(Ship, slug=ship_slug)
        ship_cost = ship.cost

        # user_resource = get_object_or_404(Resource, user=self.request.user)
        # user_resource.datacoin -= ship_cost
        # user_resource.save()

        serializer.save(user=self.request.user)
