from django.db import models
# This model is for storing & managing all crops of farmer
# CRUD for crops | disease history | harvest record | soil info per crop
from all_apps.authentication.models import Farmer

class Crops(models.Model):

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='crop')
    crop_name = models.CharField(max_length=100)
    planted_date = models.DateField(null=True, blank=True)
    area = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True) # in cent
    status = models.CharField(max_length=50,default='growing', null=True, blank=True)

    def __str__(self):
        return self.crop_name

