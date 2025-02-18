from rest_framework import serializers

from missions.models import Mission


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = (
            'id',
            'expansion',
            'name',
            'reward',
            'summary',
            'duration',
            'distance',
            'volume',
        )
