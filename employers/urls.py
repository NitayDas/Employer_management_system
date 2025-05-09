from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployerListCreateView.as_view(), name='employer-list-create'),
    path('<int:id>/', EmployerRetrieveUpdateDestroyView.as_view(), name='employer-detail'),
]