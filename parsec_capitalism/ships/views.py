from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ship, UserShip
from .serializers import BuyShipSerializer, ShipSerializer, UserShipSerializer

User = get_user_model()


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    """List of all Ships"""

    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class ListUserShipViewSet(viewsets.ReadOnlyModelViewSet):
    """To-Be Hangar endpoint"""

    def list(self, request):
        queryset = UserShip.objects.filter(user=self.request.user)
        serializer = UserShipSerializer(queryset, many=True)
        return Response(serializer.data)


class APIBuyShip(APIView):
    """Api for buying a ship. Request needs slug of a ship that is being bought."""

    def post(self, request):
        serializer = BuyShipSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # get ship instance
        ship = data['ship']

        # deduct ship's price from user's datacoins
        buyer = self.request.user
        buyer.datacoins -= ship.price
        buyer.save()

        serializer.save(user=buyer, ship=ship)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
