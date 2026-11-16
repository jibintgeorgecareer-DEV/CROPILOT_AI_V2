from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import registerAPI_Serializer, UpdateUserAPI_Serializer



def register_page_view(request):            # For render registration.html (register user)
    return render(request, 'authentication/registration.html')

class resgisterAPI_view(APIView):           # For creating a user (API)

    def post(self, request):
        
        user_details_from_html = request.data  # request.data contains the input 

        serializer = registerAPI_Serializer(data=user_details_from_html) # We call API and store JSON

        if serializer.is_valid():
            serializer.save()           # It calls the create() in registerAPI_Serializer()
            return redirect('LOGIN')

        return render(request, 'authentication/registration.html', {"error":"Username already exists"})

def login_page_view(request):   # Login | Session creation

    if request.method == "POST":
            username_input = request.POST['username']
            password_input = request.POST['password']
    
            user = authenticate(request, username=username_input, password=password_input)
    
            if user:
                login(request, user)   # Session starts
                print("User Logged:",user.username)
    
                if user.role == 'farmer':
                    return redirect('FARMER_DASH')
                
                elif user.role == 'officer':
                    return redirect('OFFICER_DASH')
                
                elif user.role == 'admin' and (user.is_staff or user.is_superuser):
                    return HttpResponse("Admin Aley!")
                
            else:
                return render(request, 'authentication/login.html', {'error':'Invalid'})

    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('LOGIN')

class UpdateUserAPI_view(APIView):   # For update user details (API)
    
    def post(self, request):

        user_details_from_html = request.data
        serializer = UpdateUserAPI_Serializer(request.user, data=request.data, partial=True)
        print("request:",request.data)

        if serializer.is_valid():
            serializer.save()
            return redirect('FARMER_PROFILE')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)