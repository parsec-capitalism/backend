from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from ships.models import Perk, Ship, UserShip, UserShipPerks

from .serializers import (
    BuyPerkSerializer,
    BuyShipSerializer,
    PerkSerializer,
    ShipSerializer,
    UserShipSerializer,
)

User = get_user_model()


class PerkViewSet(viewsets.ReadOnlyModelViewSet):
    """List of all Perks"""

    queryset = Perk.objects.all()
    serializer_class = PerkSerializer


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

        ship = data['ship']

        buyer = self.request.user
        buyer.datacoins -= ship.price
        buyer.save()

        usership = serializer.save(user=buyer, ship=ship)

        # coping perks
        ship_original_perks = ship.ship_perks.all()
        for perk in ship_original_perks:
            UserShipPerks.objects.create(
                user_ship=usership,
                perk=perk.perk,
                owned_amount=perk.default_amount,
            )

        return Response(status=status.HTTP_201_CREATED)


class APIBuyPerk(APIView):
    def post(self, request):
        serializer = BuyPerkSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user_ship = data['user_ship']
        perk = data['perk']
        amount = data['owned_amount']

        buyer = self.request.user
        buyer.datacoins -= perk.price * amount
        buyer.save()

        if user_ship.usership_perks.filter(perk=perk).exists():
            obj = UserShipPerks.objects.get(user_ship=user_ship, perk=perk)

            obj.owned_amount += amount
            obj.save()
        else:
            UserShipPerks.objects.create(
                user_ship=user_ship,
                perk=perk,
                owned_amount=amount,
            )

        return Response(status=status.HTTP_201_CREATED)
