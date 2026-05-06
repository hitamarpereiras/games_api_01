from django.urls import path, include
from rest_framework.routers import DefaultRouter
from players.views import RegisterView, PlayerViewSet


router = DefaultRouter()

router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('players/register/', RegisterView.as_view()),
    path('', include(router.urls)),
]