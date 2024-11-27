from django.contrib import admin

from .models import Player, Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
