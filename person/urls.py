from django.urls import path
from .views import *

urlpatterns = [
    path('auth/signup/', RegistrationView.as_view(), name = 'signup'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),

]