from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'game',
        'fps',
        'quality',
        'created_at',
        'updated_at'
    ]
    search_fields = [
        'user__username',
        'game__title',
        'quality',
        'fps'
    ]
