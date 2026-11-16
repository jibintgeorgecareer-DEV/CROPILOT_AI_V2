from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import predict_cocoa_disease, predict_potato_tomato_disease, predict_cardamom_disease
from .models import DiseaseReport, CropRequirements
from .serializers import DiseaseDetectionAPI_Serializer, CropRequirements_Serializer


class DiseaseDetectionAPI_View(APIView):  # Main MODULE


    def post(self, request):     # this method intercept Http POST request sent to URL

        serializer = DiseaseDetectionAPI_Serializer(data=request.data) # sent image to serializer.py

        crop_name = request.POST.get('crop_name')

        if serializer.is_valid():   # if input file EMPTY | CORRUPTED | return False

            image = serializer.validated_data['image']          

            try:
                if crop_name == 'cocoa':
                    model_result = predict_cocoa_disease(image)
                    crop_model = 'Cocoa'

                elif crop_name == 'tomato' or crop_name == 'potato':
                    model_result = predict_potato_tomato_disease(image)
                    crop_model = 'Tomato_Potato'

                elif crop_name == 'cardamom':
                    model_result = predict_cardamom_disease(image)
                    crop_model = 'Cardamom'
        
            except Exception as excep:

                print("ERROR -> ai_engine : DiseaseDetectionAPI_View --->",str(excep))
                error_messages = 'AI Model is Not Working.... please wait'
                return render(request, 'farmer/disease_result.html',{'error_messages':error_messages})

            # Storing DISEASE REPORT into DB
            DiseaseReport.objects.create(farmer=request.user.farmer, 
                crop_name='cocoa', 
                uploaded_image=image,
                detected_disease=model_result['disease'],
                confidence_score=model_result['confidence'],
                treatment=model_result['treatment']
            )

            return render(request,"farmer/disease_result.html",
            {
                "predictions": [model_result],
                "model": crop_model
            }) 
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   


class DeleteDiseaseAPI_View(APIView):

    def post(self, request, pk):

        report = DiseaseReport.objects.filter(id=pk, farmer=request.user.farmer)

        if report.exists():
            report.delete()   

            return redirect('ALL_REPORTS')

        else:
            print("ERROR -> ai_engine: Cannot Delete Disease Report! ******************")


class CropRequirements_View(APIView):  # Soil recommendation, fertilizer, climate etc...
                                       # Fetch input crop details from DB to USER
    def get(self, request):

        input_crop = request.GET.get('input_crop')

        crop_requirements_query = CropRequirements.objects.filter(crop_name=input_crop).first()

        if not crop_requirements_query:
            error_messages = "Requirements Not Found"
            return render(request, 'farmer/crop_requirements.html', {'error_messages':error_messages})

        serializer = CropRequirements_Serializer(crop_requirements_query)

        result = serializer.data

        return render(request, 'farmer/crop_requirements.html', {'result':result})
