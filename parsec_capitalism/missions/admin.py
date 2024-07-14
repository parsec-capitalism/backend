from django.contrib import admin
from .models import Missions


@admin.register(Missions)
class MissionsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
