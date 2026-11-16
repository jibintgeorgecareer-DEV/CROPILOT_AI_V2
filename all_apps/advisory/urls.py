from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.FarmerMessage_API.as_view(), name='CHAT'),
]
