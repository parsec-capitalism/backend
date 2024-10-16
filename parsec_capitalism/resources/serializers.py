from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Resource
        fields = ('id', 'user', 'datacoin', 'quantium')
