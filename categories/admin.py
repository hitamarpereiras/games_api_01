from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'created_at'
    ]
    search_fields = [
        'id',
        'name'
    ]
