from processors.models import Processor
from rest_framework import serializers


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fileds = [
            'id',
            'manufacturer',
            'modelo',
            'generation',
            'year',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]