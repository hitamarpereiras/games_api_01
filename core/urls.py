from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('api/', include('players.urls')),
    path('api/', include('categories.urls')),
    path('api/', include('games.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('game_requirements.urls')),
    path('api/', include('processors.urls')),
    path('api/', include('gpus.urls')),
]
