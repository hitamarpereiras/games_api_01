from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from processors.models import Processor
from processors.serializers import ProcessorSerializer


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ProcessorViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Processor.objects.all().order_by('-created_at')
    serializer_class = ProcessorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Procura exatamente igual ou contém o valor ignorando maiúsculas e minúsculas
    filterset_fields = {
        'manufacturer': ['exact', 'icontains'], 
        'modelo': ['exact', 'icontains'],
        'generation': ['exact', 'icontains'],
        'year': ['exact', 'gte', 'lte'],
    }

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Processor.objects.all().order_by('-created_at')

        if self.action in ['list', 'retrieve']:
            return Processor.objects.all().order_by('-created_at')

        return Processor.objects.none()


