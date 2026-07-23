from django.contrib import admin
from processors.models import Processor


@admin.register(Processor)
class ProcessorAdmin(admin.AdminSite):
    list_display= [
        'id',
        'manufacturer',
        'modelo',
        'generation',
        'yaer',
        'creadted_at'
    ]
    search_fields= [
        'manufacturer',
        'modelo',
        'generation'
    ]
    
