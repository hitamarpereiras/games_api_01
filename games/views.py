from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from games.models import Game
from games.serializers import GameSerializer
from rest_framework.parsers import MultiPartParser, FormParser
 

from services.validators import validate_image
from services.pillow_svc import process_image
from services.supabase_svc import upload_image
from services.supabase_svc import delete_image


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class GameViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all().order_by('-created_at')
    serializer_class = GameSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_fields = {
        'name': ['icontains'],
        'category__name': ['icontains'],
        'score': ['exact', 'gte', 'lte'],
        'release_date': ['exact', 'gte', 'lte'],
    }


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        
        return [IsAuthenticated()]


    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Game.objects.all().order_by('-created_at')
        
        return Game.objects.filter(user=self.request.user).order_by('-created_at')
    

    def create(self, request, *args, **kwargs):
        image = request.FILES.get('image_cover')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cover_url = None
        cover_path = None

        if image:
            try:
                validate_image(image)
                buffer, ext = process_image(image, 720, 1024)

                upload = upload_image(
                    file_bytes=buffer.getvalue(),
                    ext=ext,
                    bucket='covers_games'
                )

                cover_url = upload["url"]
                cover_path = upload["path"]

            except Exception as e:
                return Response(
                    {"message": f"Erro ao processar a imagem: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        user = request.user
        
        serializer.save(
            user=user,
            cover_url=cover_url,
            cover_path=cover_path
        )

        return Response(
            {"message": "Criado com sucesso"},
            status=status.HTTP_201_CREATED
        )
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
            )
        serializer.is_valid(raise_exception=True)

        image = request.FILES.get('image_cover')

        if image:
            try:
                validate_image(image)

                if instance.cover_path:
                    delete_image(
                        path=instance.cover_path,
                        bucket='covers_games'
                    )

                buffer, ext = process_image(image, 720, 1024)

                upload = upload_image(
                    file_bytes=buffer.getvalue(),
                    ext=ext,
                    bucket='covers_games'
                )

                cover_url = upload["url"]
                cover_path = upload["path"]

            except Exception as e:
                return Response(
                    {"message": f"Erro ao processar a imagem: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        user = request.user

        extra_data = {"user": user}

        if image:
            extra_data.update({
                "cover_url": cover_url,
                "cover_path": cover_path
            })
        
        serializer.save(**extra_data)

        return Response(
            {"message": "Atualizado com sucesso"},
            status=status.HTTP_200_OK
        )
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.cover_path:
            delete_image(
                path=instance.cover_path,
                bucket='covers_games'
            )

        instance.delete()

        return Response(
            {"message": "Deletado com sucesso"},
            status=status.HTTP_204_NO_CONTENT
        )