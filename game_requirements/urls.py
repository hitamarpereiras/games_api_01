from django.urls import path, include
from rest_framework.routers import DefaultRouter
from game_requirements.views import GameRequirementViewSet

router = DefaultRouter()
router.register(r'requirements', GameRequirementViewSet)

urlpatterns = [
    path('', include(router.urls))
]