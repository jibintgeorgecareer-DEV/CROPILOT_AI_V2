from django.urls import path
from . import views

urlpatterns = [

    path('api-disease-detect/',views.DiseaseDetectionAPI_View.as_view(),name='API_DISEASE_DETECT'),
    
    path('api-delete-disease/<int:pk>/', views.DeleteDiseaseAPI_View.as_view(), name='API_DELETE_DISEASE'),

    path('api-crop-requirements/', views.CropRequirements_View.as_view(), name='API_CROP_REQUIREMENTS'),
]