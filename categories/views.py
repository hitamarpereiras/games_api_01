from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all().order_by('created_at')
    serializer_class = CategorySerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsAuthenticated()]