from djoser.conf import settings
from djoser.serializers import UserCreateSerializer
from resources.models import Resource
from rest_framework import serializers

from .models import Ship, User, UserShip

STARTER_DATACOINS = 666
STARTER_QUANTUIM = 100


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
    ship = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Ship.objects.all()
    )

    class Meta:
        model = UserShip
        fields = ('id', 'user', 'ship', 'on_mission')


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        Resource.objects.create(
            user=user,
            datacoin=STARTER_DATACOINS,
            quantium=STARTER_QUANTUIM
        )
        return user
