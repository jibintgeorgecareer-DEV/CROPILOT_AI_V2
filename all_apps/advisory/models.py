from django.db import models
from all_apps.authentication.models import Farmer, Officer

# Create your models here.

class Advisory(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)   # message From
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE) # message To

    image = models.ImageField(upload_to='advisory_images/',blank=True,null=True)
    question = models.TextField(blank=True, null=True)          # farmer ask
    answer = models.TextField(blank=True, null=True)  # officer reply
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

