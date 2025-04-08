from rest_framework import serializers

from missions.models import Mission, PlayerMission


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'


class PlayerMissionLogSerializer(serializers.ModelSerializer):
    mission_name = serializers.CharField(source='mission.name', read_only=True)
    ship_name = serializers.CharField(source='ship.ship.name', read_only=True)

    class Meta:
        model = PlayerMission
        fields = ['id', 'mission_name', 'ship_name', 'start_time', 'finish_time', 'reward', 'status']
        read_only_fields = fields
