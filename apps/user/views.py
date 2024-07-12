from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PatientSerializer
from .models import Patient
from rest_framework import generics
# Create your views here.

class PatientView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
