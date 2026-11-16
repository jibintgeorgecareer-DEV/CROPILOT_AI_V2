from rest_framework import serializers
from .models import Crops

class AddCropsAPI_Serializer(serializers.ModelSerializer):    # To add crops

    class Meta:
        model = Crops
        fields = ['crop_name','planted_date','area','status']

    def create(self, validated_data):
        request = self.context['request']
        
        print("AddCropsAPI_Serializer:", request.user.farmer)


        crop = Crops.objects.create(farmer=request.user.farmer, 
        crop_name=validated_data['crop_name'], planted_date=validated_data['planted_date'],
        area=validated_data['area'], status=validated_data['status']
        )
        return crop

class ListCropsAPI_Serializer(serializers.ModelSerializer):   # To list all crops of farmer.

    class Meta:
        model = Crops
        fields = ['crop_name','planted_date','area','status']