from django.db import models

# Create your models here.

class CropMarketPrice(models.Model):
    crop_name = models.CharField(max_length=50)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    updated_at = models.DateTimeField(auto_now_add=True)

    source = models.CharField(max_length=100, blank=True)