
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics 
from .models import Prescription
from .serializers import PrescriptionSerializer
# Create your views here.

class PrescriptionView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer




