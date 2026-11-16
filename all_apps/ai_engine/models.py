from django.db import models
from all_apps.authentication.models import Farmer

# Create your models here.

class DiseaseReport(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100)
    uploaded_image = models.ImageField(upload_to='crop_images/')
    detected_disease = models.CharField(max_length=100)
    confidence_score = models.FloatField(null=True, blank=True)   
    treatment = models.TextField(blank=True)
    verified_by_officer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop_name} - {self.detected_disease}"


class ChatBotHistory(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farmer_query = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Recommend soil, fertilizer, ph-value etc.. (Crop data to store)
class CropRequirements(models.Model):
    crop_name = models.CharField(max_length=100, unique=True)
    suitable_soil = models.TextField()
    ph_value = models.CharField(max_length=50)
    reason = models.TextField()
    suitable_climate = models.TextField()
    fertilizer = models.TextField()
    temprature = models.CharField(max_length=50)
    rainfall = models.CharField(max_length=100)
    crucial_factor = models.TextField()

    def __str__(self):
        return self.crop_name