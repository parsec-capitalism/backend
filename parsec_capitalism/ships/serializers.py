from rest_framework import serializers

from .models import Ship, User, UserShip

STARTER_DATACOINS = 666
STARTER_QUANTUIM = 100


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('slug', 'name', 'price', 'cargo_weight', 'cargo_volume', 'range')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        ref_name = 'ReadOnlyUsers'


class UserShipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    ship = serializers.SlugRelatedField(slug_field='slug', queryset=Ship.objects.all())

    class Meta:
        model = UserShip
        fields = ('id', 'user', 'ship', 'on_mission')
