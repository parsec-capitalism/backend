from django.urls import path

from . import views

app_name = 'ships'

urlpatterns = [
    path('', views.ships_list, name='ships_list'),
]
