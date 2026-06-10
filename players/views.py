from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from players.models import Player
from players.serializers import RegisterSerializer, PlayerSerializer
from rest_framework.parsers import MultiPartParser, FormParser


from services.users_svc import UserService
from services.validators import validate_image
from services.pillow_svc import process_image
from services.supabase_svc import upload_image
from services.supabase_svc import delete_image


class RegisterView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        UserService.register_player(serializer.validated_data)

        return Response(
            {"message": "Usuário criado com sucesso"},
            status=status.HTTP_201_CREATED
        )


class PlayerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Player.objects.all().order_by('-created_at')
    serializer_class = PlayerSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Player.objects.filter(user=self.request.user)
        else:
            return Player.objects.none()
        
    def create(self, request, *args, **kwargs):
        image = request.FILES.get('image')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if image:
            try:
                validate_image(image)
                buffer, ext = process_image(image, 300, 300)

                upload = upload_image(
                    file_bytes=buffer.getvalue(),
                    ext=ext,
                    bucket='users_avatars'
                )

                avatar_url = upload["url"]
                avatar_path = upload["path"]

            except Exception as e:
                return Response(
                    {"message": f"Erro ao processar a imagem: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer.save(
            avatar_url=avatar_url,
            avatar_path=avatar_path
        )

        return Response(
            {"message": "Usuario criado com sucesso"},
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

        image = request.FILES.get('image')

        avatar_url = None
        avatar_path = None

        if image:
            try:
                validate_image(image)

                if instance.avatar_path:
                    delete_image(
                        path=instance.avatar_path,
                        bucket='users_avatars'
                    )

                buffer, ext = process_image(image, 300, 300)

                upload = upload_image(
                    file_bytes=buffer.getvalue(),
                    ext=ext,
                    bucket='users_avatars'
                )

                avatar_url = upload["url"]
                avatar_path = upload["path"]

            except Exception as e:
                return Response(
                    {"message": f"Erro ao processar a imagem: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        serializer.save(
            avatar_url=avatar_url,
            avatar_path=avatar_path
        )

        return Response(
            {"message": "Usuario atualizado com sucesso"},
            status=status.HTTP_200_OK
        )
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.avatar_path:
            delete_image(
                path=instance.avatar_path,
                bucket='users_avatars'
            )

        instance.delete()

        return Response(
            {"message": "Usuario deletado com sucesso"},
            status=status.HTTP_204_NO_CONTENT
        )