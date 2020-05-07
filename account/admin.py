from django.contrib import admin
from .models import FarmerProfile


@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'farm_name',
                    'city', 'state', 'status', 'went_public', ]
    list_filter = ('status', 'went_public')
    search_fields = ('farmer', 'farm_name')
    date_hierarchy = 'went_public'
    ordering = ('status', 'went_public')
