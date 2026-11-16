from django.db import models
from django.contrib.auth.models import AbstractUser

# Just to store every users ROLE, PHONE
class CustomUser(AbstractUser): 
    ROLES_CHOICES = (
        ('admin', 'Admin'),
        ('officer', 'Agriculture Officer'),
        ('farmer', 'Farmer'),
    )

    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default='farmer')
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"


# Detailed table for Farmer
class Farmer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='farmer')
    age = models.IntegerField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='farmer_images/',blank=True)
    aadhaar = models.CharField(max_length=20, blank=True, null=True) # aadhar number

    district = models.CharField(max_length=100, null=True, blank=True) # location
    region = models.CharField(max_length=100, null=True, blank=True) # location
    address = models.TextField(blank=True)
    panchayath = models.CharField(max_length=100, null=True, blank=True)

    farm_size = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True) # in cent
    farm_type = models.CharField(max_length=25, null=True, blank=True) 
    # ABOVE: paddy, vegetables, livestock, mixed farming
    soil_type = models.CharField(max_length=25, null=True, blank=True)
    soil_card = models.ImageField(upload_to='soilcard_images',blank=True,) # Soil card images of farmer

    officer_assigned = models.ForeignKey('Officer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.user.role})"
    

# Detailed table of Agriculture officer (All details)
class Officer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='officer')

    office_district = models.CharField(max_length=100, null=True, blank=True) # location
    office_region = models.CharField(max_length=100, null=True, blank=True) # location
    panchayath = models.CharField(max_length=100, null=True, blank=True)

    whatsapp_number = models.CharField(max_length=12, blank=True, null=True)
    profile_image = models.ImageField(upload_to='officer_images/',blank=True) # profile pic

    employee_id = models.CharField(max_length=10, unique=True)  # Service, Govnt ID
    designation = models.CharField(max_length=25, blank=True, null=True) # Assistant, Agri Officer
    qualification = models.CharField(max_length=255, blank=True, null=True) # Bsc, Msc, 
    experience = models.IntegerField(null=True, blank=True)

    start_time = models.TimeField(default="09:00:00")  # Office timing
    end_time = models.TimeField(default="17:00:00")

    def __str__(self):
        return f"{self.user.username} ({self.user.role})"