from django.contrib.auth.models import User
from django.db import transaction
from players.models import Player

from services.validators import validate_image
from services.pillow_svc import process_image
from services.supabase_svc import upload_image


class UserService:

    @staticmethod
    @transaction.atomic
    def register_player(validated_data):

        image = validated_data.pop("image", None)
        
        #Cria User + Player em uma transação atômica
        
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        # Criar User
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Criar Player
        player = Player.objects.create(
            user=user,
            **validated_data
        )

        if image:
            validate_image(image)

            buffer, ext = process_image(image, 300, 300)

            upload = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket='users_avatars'
            )

            player.avatar_url = upload["url"]
            player.avatar_path = upload["path"]
            player.save()

        return player