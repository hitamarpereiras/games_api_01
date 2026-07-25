from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from gpus.models import Gpu
from gpus.serializers import GpuSerializers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class GpuViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Gpu.objects.all().order_by('-created_at')
    serializer_class = GpuSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Procura exatamente igual ou contém o valor ignorando maiúsculas e minúsculas
    filterset_fields = {
        'manufacturer': ['exact', 'icontains'], 
        'modelo': ['exact', 'icontains'],
        'vram': ['exact', 'gte', 'lte'],
    }

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Gpu.objects.all().order_by('-created_at')

        if self.action in ['list', 'retrieve']:
            return Gpu.objects.all().order_by('-created_at')

        return Gpu.objects.none()
