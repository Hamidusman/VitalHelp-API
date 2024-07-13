from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PatientSerializer, DoctorSerializer
from .models import Patient, Doctor
from rest_framework import generics, viewsets
# Create your views here.


class PatientViewSet(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorView(generics.ListCreateAPIView):
    queryset  = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorViewSet(viewsets.GenericViewSet):
    queryset = Doctor.objects.all()