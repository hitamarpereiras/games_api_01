from django.contrib import admin
from gpus.models import Gpu


@admin.register(Gpu)
class GpuAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'manufacturer',
        'modelo'
    ]
    search_fields= [
        'manufacturer',
        'modelo'
    ]
