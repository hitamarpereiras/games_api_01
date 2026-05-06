from django.urls import path, include
from rest_framework.routers import DefaultRouter
from games.views import GameViewset


router = DefaultRouter()
router.register(r'games', GameViewset)

urlpatterns = [
    path('', include(router.urls))
]