from django.contrib import admin
from game_requirements.models import Requirement

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = [
        'game',
        'system',
        'minimum_processor',
        'minimum_ram',
        'minimum_gpu',
        'minimum_gpu_ram',
        'maximum_processor',
        'maximum_ram',
        'maximum_gpu',
        'maximum_gpu_ram',
        'created_at',
    ]
    search_fields = ['game']
    list_filter = ['created_at']
