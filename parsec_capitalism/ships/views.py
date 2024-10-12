from rest_framework import viewsets

from .models import Ship, User, UserShip
from .serializers import ShipSerializer, UserSerializer, UserShipSerializer


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserShipViewSet(viewsets.ModelViewSet):
    queryset = UserShip.objects.all()
    serializer_class = UserShipSerializer
