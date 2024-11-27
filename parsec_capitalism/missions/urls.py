from rest_framework import routers

app_name = 'missions'
router = routers.DefaultRouter()
# router.register(r'missions', views.ShipViewSet)

urlpatterns = [
    # path('', views.missions_list, name='ships_list'),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
