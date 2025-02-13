from rest_framework import serializers

from ships.models import Ship, UserShip


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = (
            'slug',
            'name',
            'price',
            'cargo_weight',
            'cargo_volume',
            'range',
            'id',
        )


class BuyShipSerializer(serializers.ModelSerializer):
    ship = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Ship.objects.all(),
    )
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserShip
        fields = ('id', 'user', 'ship', 'on_mission')


class UserShipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    ship = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Ship.objects.all(),
    )

    class Meta:
        model = UserShip
        fields = ('id', 'user', 'ship', 'on_mission')
