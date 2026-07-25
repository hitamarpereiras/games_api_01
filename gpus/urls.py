from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gpus.views import GpuViewSets


router = DefaultRouter()

router.register(r'gpus', GpuViewSets)

urlpatterns = [
    path('', include(router.urls)),
]