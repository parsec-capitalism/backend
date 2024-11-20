from django.contrib import admin

from .models import Ship, UserShip


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


admin.site.register(Ship, ShipsAdmin)
admin.site.register(UserShip)
