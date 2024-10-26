from django.contrib import admin
from .models import Resource


class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'datacoin',
        'quantium',
    )

    list_editable = (
        'datacoin',
        'quantium',
    )

    list_display_links = ('user',)


# Register your models here.
admin.site.register(Resource, ResourceAdmin)
