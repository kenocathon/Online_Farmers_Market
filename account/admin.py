from django.contrib import admin
from .models import FarmerProfile


@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'farm_name', 'farm_description',
                    'farm_products', 'farm_photo']
