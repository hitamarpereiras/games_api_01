from django.contrib import admin
from players.models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        'user__username',
        'processor',
        'memory_ram',
        'disk',
        'disk_space',
        'unit',
        'gpu_name',
        'gpu_memory',
        'created_at'
    ]
    search_fields = [
        'user__username',
    ]
