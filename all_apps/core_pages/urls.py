from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page_view, name='INDEX'), # Open the index page

    path('homepage/', views.farmer_dash_view, name='FARMER_DASH'), # to farmer Dash

    path('profile/', views.farmer_profile_view, name='FARMER_PROFILE'),
    path('edit_profile/', views.farmer_edit_profile, name='EDIT_PROFILE'),

    path('all_crops/', views.all_crops, name='ALL_CROPS'),

    path('disease_detection/', views.disease_detection, name='DISEASE_DETECTION'),
    path('all_reports/', views.all_reports, name='ALL_REPORTS'),

    path('crop_requirements/', views.crop_requirements, name='CROP_REQUIREMENTS'),

    path('advisory/', views.advisory, name='ADVISORY'),

    path('market/', views.market_price, name='MARKET_PRICES'),

    path('feedback/', views.feedback_view, name='FEEDBACK'),
    path('api-feedback/', views.FeedbackAPI_Views.as_view(), name='API_FEEDBACK'),

]