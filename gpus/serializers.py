from gpus.models import Gpu
from rest_framework import serializers


class GpuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = [
            'id',
            'manufacturer',
            'modelo',
            'year',
            'vram',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]