from rest_framework import serializers
from .models import Ship, User, UserShip


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ['id', 'title', 'cost', 'size', 'slug']


class UserSerializer(serializers.ModelSerializer):
    # cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        ref_name = 'ReadOnlyUsers'


class UserShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShip
        fields = ['id', 'user', 'ship', 'on_mission']
