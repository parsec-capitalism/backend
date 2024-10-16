from rest_framework import serializers
from .models import Ship, User, UserShip


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('id', 'title', 'cost', 'size', 'slug')


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
