from django.db import models
from django.conf import settings


class FarmerProfile(models.Model):
    farmer = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=8)
    farm_description = models.TextField()
    farm_products = models.TextField()
    farm_photo = models.ImageField(upload_to='farmers/', blank=True)

    def __str__(self):
        return f'Profile for farmer {self.farmer.username}'
