from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Advisory
from all_apps.authentication.models import Farmer

class FarmerMessage_API(APIView):

    def post(self, request):

        question = request.POST.get('question')
        msg_image = request.POST.get('msg_image')

        assigned_officer = request.user.farmer.officer_assigned

        Advisory.objects.create(
            farmer=request.user.farmer, 
            officer = assigned_officer,
            question = question,
            image = msg_image,
        )

        return redirect('ADVISORY')