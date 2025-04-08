from django.contrib import admin

from .models import Mission, PlayerMission


@admin.register(Mission)
class MissionsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PlayerMission)
class PlayerMissionAdmin(admin.ModelAdmin):
    list_display = ('player', 'mission', 'ship', 'start_time', 'finish_time', 'status', 'reward')
    list_filter = ('status', 'start_time')
    search_fields = ('player__username', 'mission__name')
    readonly_fields = ('start_time',)
