from django.db import models
from all_apps.authentication.models import CustomUser
# Create your models here.

class Feedback(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
