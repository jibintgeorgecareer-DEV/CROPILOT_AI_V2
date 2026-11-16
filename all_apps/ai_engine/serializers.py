from rest_framework import serializers
from .models import CropRequirements

# serializer just validating input image FILE
class DiseaseDetectionAPI_Serializer(serializers.Serializer):

    image = serializers.ImageField()   # It validates the input is a image file | It validates
                                       # the uploaded file is graphic img (JPEG, PNG)


class CropRequirements_Serializer(serializers.ModelSerializer):

    class Meta:
        model = CropRequirements
        fields = ['id','crop_name','suitable_soil','ph_value','reason','suitable_climate',
            'fertilizer','temprature','rainfall','crucial_factor'
        ]