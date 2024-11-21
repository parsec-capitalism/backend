from django.contrib import admin

from .models import Perk, Ship, UserShip


@admin.register(Ship)
class ShipsAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'price',
        'cargo_weight',
        'cargo_volume',
        'range',
    )

    list_display_links = ('name',)


@admin.register(Perk)
class PerksAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'num_value',
        'bool_value',
    )

    list_display_links = ('name',)


@admin.register(UserShip)
class UserShipAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'ship',
        'on_mission',
    )
