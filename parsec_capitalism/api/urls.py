from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('', include('api.ships.urls')),
    path('', include('api.players.urls')),
    path('', include('api.missions.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
