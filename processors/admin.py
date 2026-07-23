from django.contrib import admin
from processors.models import Processor


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'manufacturer',
        'modelo',
        'generation',
    ]
    search_fields= [
        'manufacturer',
        'modelo',
        'generation'
    ]
    
