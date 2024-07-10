from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import generics
# Create your views here.

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer