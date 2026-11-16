from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddCropsAPI_Serializer, ListCropsAPI_Serializer
from all_apps.crops_management.models import Crops

class AddCropsAPI_View(APIView):

    def post(self, request):

        crop_details_input = request.data
                                                   
        serializer = AddCropsAPI_Serializer(data=crop_details_input, context={'request':request})

        if serializer.is_valid():
            serializer.save()
            return redirect('ALL_CROPS')

        print("ERROR -> crops_management / AddCropsAPI_View")
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class DeleteCropAPI_View(APIView):

    def post(self, request, pk):

        try:
            crop = Crops.objects.get(id=pk, farmer=request.user.farmer)
            crop.delete()

            print("OKEY -> crop_management / DeleteCropAPI_View : Crop Deleted")
            messages.success(request, "Crop Deleted")
            return redirect('ALL_CROPS')
        
        except Crops.DoesNotExist:
            print("NOT FOUND -> crop_management / DeleteCropAPI_View : Crop not found")
            error_messages = "Crop Not Found"
            return render(request, 'farmer/add_crops.html', {'error_messages':error_messages})
