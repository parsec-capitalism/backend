from django.contrib import admin

from .models import Ship, UserShip


class ShipsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cost',
        'size',
        'slug'
    )

    list_editable = (
        'cost',
        'size',
        'slug'
    )

    list_display_links = ('title',)



# Register your models here.
admin.site.register(Ship, ShipsAdmin)
admin.site.register(UserShip)
