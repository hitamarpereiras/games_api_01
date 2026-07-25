from django.contrib import admin
from games.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'get_categories',
        'release_date',
        'created_at',
    ]
    search_fields = [
        'name',
        'category__name',
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('category')

    def get_categories(self, obj):
        return ", ".join(c.name for c in obj.category.all())
    
    get_categories.short_description = "Categorias"