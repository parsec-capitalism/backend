from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'ships'
router = routers.DefaultRouter()
router.register(r'ships-api', views.ShipViewSet)

urlpatterns = [
    path('', views.ships_list, name='ships_list'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
