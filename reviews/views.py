from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from reviews.models import Review
from reviews.serializers import ReviewSerializer


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class ReviewViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['game']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            username=self.request.user.username
        )
        return super().perform_create(serializer)