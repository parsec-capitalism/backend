from rest_framework import serializers
from .models import Resource, User


class ResourceSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Resource
        fields = ('id', 'user', 'datacoin', 'quantium')
