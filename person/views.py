from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *
# from .permissions import ISOwner



class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    
    


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user