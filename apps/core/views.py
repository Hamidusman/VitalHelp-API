from rest_framework.permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from apps.user.models import Patient
from .models import Prescription
from .serializers import PrescriptionSerializer
# Create your views here.

class PrescriptionView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer





'''
    def get_query(self):
        user = self.request.user
        if user.is_staff:
            patient_id = self.request.query_params.get('patient_id')
            if patient_id:
                try:
                    patient = Patient.objects.get(pk=patient_id) 
                    return Prescription.objects.filter(patient=patient)
                except Patient.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Prescription.objects.none() 
        else:
            return Prescription.objects.filter(patient=user.patient)
'''