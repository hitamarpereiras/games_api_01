from players.models import Player
from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    image = serializers.ImageField(write_only=True, required=False)
    
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    processor = serializers.CharField()
    memory_ram = serializers.IntegerField()
    disk = serializers.CharField()
    disk_space = serializers.IntegerField()
    gpu_name = serializers.CharField()
    gpu_memory = serializers.IntegerField()


class PlayerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Player
        fields = [
            'id',
            'username',
            'avatar_url',
            'processor',
            'memory_ram',
            'disk',
            'disk_space',
            'unit',
            'gpu_name',
            'gpu_memory',
            'image',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'avatar_url',
            'avatar_path',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        validated_data.pop('image', None)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('image', None)
        return super().update(instance, validated_data)
