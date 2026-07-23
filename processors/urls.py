from django.urls import path, include
from rest_framework.routers import DefaultRouter
from processors.views import ProcessorViewset


router = DefaultRouter()

router.register(r'processors', ProcessorViewset)

urlpatterns = [
    path('', include(router.urls)),
]