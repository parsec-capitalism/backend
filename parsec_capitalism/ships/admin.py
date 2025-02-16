from django.contrib import admin

from .models import Perk, Ship, UserShip


@admin.register(Perk)
class PerksAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_display_links = ('name',)


class ShipPerkInline(admin.TabularInline):
    model = Ship.perks.through


@admin.register(Ship)
class ShipsAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'price',
    )
    inlines = [ShipPerkInline]

    list_display_links = ('name',)


class UserShipPerkInline(admin.TabularInline):
    model = UserShip.perks.through


@admin.register(UserShip)
class UserShipAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'ship',
        'on_mission',
    )

    inlines = [UserShipPerkInline]
