from rest_framework import serializers

from ships.models import Perk, Ship, ShipPerks, UserShip, UserShipPerks


class PerkSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = [
            'name',
        ]


class ShipPerkSerializer(serializers.ModelSerializer):
    perk = PerkSnippetSerializer(read_only=True)

    class Meta:
        model = ShipPerks
        fields = [
            'perk',
            'default_amount',
        ]


class UserShipPerkSerializer(serializers.ModelSerializer):
    perk = PerkSnippetSerializer(read_only=True)

    class Meta:
        model = UserShipPerks
        fields = [
            'perk',
            'owned_amount',
        ]


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


class UserShipSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    # ship = serializers.SlugRelatedField(
    #     slug_field='slug',
    #     queryset=Ship.objects.all(),
    # )

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
