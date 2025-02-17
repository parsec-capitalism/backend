from rest_framework import serializers

from ships.models import Ship, ShipPerks, UserShip, UserShipPerks


class ShipPerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipPerks
        fields = [
            'perk',
            'default_amount',
        ]
        depth = 1


class UserShipPerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShipPerks
        fields = [
            'perk',
            'owned_amount',
        ]
        depth = 1


class ShipSerializer(serializers.ModelSerializer):
    perks = ShipPerkSerializer(
        source='ship_perks',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ship
        fields = (
            'id',
            'slug',
            'name',
            'price',
            'range',
            'cargo_hold',
            'perks',
        )


class UserShipSerializer(serializers.ModelSerializer):
    perks = UserShipPerkSerializer(
        source='usership_perks',
        many=True,
        read_only=True,
    )

    class Meta:
        model = UserShip
        fields = (
            'id',
            'ship',
            'on_mission',
            'perks',
        )
        depth = 1


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
        fields = (
            'id',
            'user',
            'ship',
            'on_mission',
        )


class BuyPerkSerializer(serializers.ModelSerializer):
    # user_ship = serializers.SlugRelatedField(
    #     slug_field='slug',
    #     queryset=Ship.objects.all(),
    # )

    class Meta:
        model = UserShipPerks
        fields = (
            'user_ship',
            'perk',
            'owned_amount',
        )
