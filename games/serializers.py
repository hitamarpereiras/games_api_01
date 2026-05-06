from games.models import Game
from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):

    image_cover = serializers.ImageField(write_only=True, required=False)

    category = CategorySerializer(many=True, read_only=True)

    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Category.objects.all().order_by('created_at'),
        source='category'
    )

    class Meta:
        model = Game
        fields = [
            'id',
            'user',
            'name',
            'category',
            'category_ids',
            'release_date',
            'description',
            'cover_url',
            'score',
            'image_cover',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]


    def create(self, validated_data):
        categories = validated_data.pop('category', [])
        validated_data.pop('image_cover', None)

        game = Game.objects.create(**validated_data)
        game.category.set(categories)

        return game

    def update(self, instance, validated_data):
        categories = validated_data.pop('category', None)
        validated_data.pop('image_cover', None)

        if categories is not None:
            instance.category.set(categories)

        return super().update(instance, validated_data)