from django.shortcuts import render, redirect
from all_apps.crops_management.models import Crops
from all_apps.ai_engine.models import DiseaseReport
from all_apps.advisory.models import Advisory
from all_apps.authentication.models import Farmer, Officer
from all_apps.crop_prices.models import CropMarketPrice

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FeedbackAPI_Serializer
from all_apps.authentication.decorators import role_required
# Create your views here.

def index_page_view(request):
    return render(request, 'index.html')

@role_required(['farmer'])
def farmer_dash_view(request):
    crops = Crops.objects.filter(farmer=request.user.farmer).count()
    reports = DiseaseReport.objects.filter(farmer=request.user.farmer).count()
    return render(request, 'farmer/dashboard.html', {'crops':crops,'reports':reports})

@role_required(['farmer'])
def farmer_profile_view(request):
    crops = Crops.objects.filter(farmer=request.user.farmer)
    reports = DiseaseReport.objects.filter(farmer=request.user.farmer)
    return render(request, 'farmer/profile.html', {'crops':crops, 'reports':reports})

@role_required(['farmer'])
def farmer_edit_profile(request):
    return render(request, 'farmer/edit_profile.html')

@role_required(['farmer'])
def all_crops(request):
    crops = Crops.objects.filter(farmer=request.user.farmer)
    return render(request, 'farmer/add_crops.html', {'crops':crops})

def disease_detection(request):
    return render(request, 'farmer/disease_detection.html')

@role_required(['farmer'])
def all_reports(request):
    reports = DiseaseReport.objects.filter(farmer=request.user.farmer)
    return render(request, 'farmer/all_results.html', {'reports':reports})

@role_required(['farmer'])
def crop_requirements(request):
    return render(request, 'farmer/crop_requirements.html')

@role_required(['farmer'])
def advisory(request):
    msg = Advisory.objects.filter(farmer=request.user.farmer).order_by('created_at')
    officer = request.user.farmer.officer_assigned
        
    return render(request, 'farmer/advisory.html', {'msg':msg, 'officer':officer})

@role_required(['farmer'])
def market_price(request):
    price = CropMarketPrice.objects.all()
    return render(request, 'farmer/market_prices.html',{'price':price})

@role_required(['farmer'])
def feedback_view(request):
    return render(request, 'farmer/feedback.html')

class FeedbackAPI_Views(APIView):

    def post(self, request):

        text = request.data

        serialzer = FeedbackAPI_Serializer(data=text, context={'request':request})

        if serialzer.is_valid():
            serialzer.save()

            return redirect('FARMER_DASH')

        return Response(serialzer.errors)
        