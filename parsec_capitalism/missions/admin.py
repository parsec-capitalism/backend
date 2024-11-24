from django.contrib import admin

from .models import Mission


@admin.register(Mission)
class MissionsAdmin(admin.ModelAdmin):
    list_display = ('codename',)
