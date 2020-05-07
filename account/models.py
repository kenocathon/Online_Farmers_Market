from django.db import models
from django.conf import settings
from django.utils import timezone


class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(status='public')


class FarmerProfile(models.Model):
    STATUS_CHOICES = (
        ('not public', 'Not Public'),
        ('public', 'Public')
    )
    farmer = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=8)
    farm_name = models.CharField(max_length=50)
    farm_description = models.TextField()
    farm_products = models.TextField()
    farm_photo = models.ImageField(upload_to='farmers/', blank=True)
    went_public = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='not public')
    is_public = PublicManager()

    class Meta:
        ordering = ('-went_public',)

    def __str__(self):
        return f'Profile for farmer {self.farmer.username}'

    def get_absolute_url(self):
        return reverse('home:post_detail', args[self.farmer, self.farm_name])
