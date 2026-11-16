from django.urls import path
from . import views

urlpatterns = [

    path('api-crop-add/', views.AddCropsAPI_View.as_view(), name='API_ADD_CROP'), # Add crops
    
    path('api-crop-delete/<int:pk>', views.DeleteCropAPI_View.as_view(), name='API_DELETE_CROP'),
]