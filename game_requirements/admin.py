from django.contrib import admin
from game_requirements.models import Requirement

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = [
        'game',
        'system',
        'created_at',
    ]
    search_fields = ['game']
    list_filter = ['created_at']
