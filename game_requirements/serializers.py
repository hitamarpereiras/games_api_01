from rest_framework.serializers import ModelSerializer
from game_requirements.models import Requirement


class GameRequirementSerializer(ModelSerializer):
    class Meta:
        model = Requirement
        fields = [
            'id',
            'game',
            'minimum_processor',
            'minimum_ram',
            'minimum_gpu',
            'minimum_gpu_ram',
            'maximum_processor',
            'maximum_ram',
            'maximum_gpu',
            'maximum_gpu_ram',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]