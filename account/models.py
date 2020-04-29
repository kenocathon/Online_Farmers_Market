from django.db import models
from django.conf import settings


class FarmerProfile(models.Model):
    farmer = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    farm_description = models.TextField()
    farm_products = models.TextField()
    farm_photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for farmer {self.farmer.username}'
