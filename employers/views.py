from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import IsEmployerOwner




class EmployerListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class EmployerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployerOwner]
    lookup_field = 'id'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)