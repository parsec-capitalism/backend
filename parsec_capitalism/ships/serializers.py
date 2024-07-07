from rest_framework import serializers
from ships.models import Ships


class ShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ships
        fields = ['title', 'cost', 'size', 'slug']
