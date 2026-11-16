from django.urls import path
from . import views

urlpatterns = [

    path('registration', views.register_page_view, name='REGISTER'), # Open registraion.html
    path('api-register/', views.resgisterAPI_view.as_view(), name='API_REGISTER'), # API registration

    path('login/', views.login_page_view, name='LOGIN'),   # Open login page
    path('logout/', views.logout_view, name='LOGOUT'),

    path('api-edit/', views.UpdateUserAPI_view.as_view(), name='EDIT_PROFILE_API'),
]