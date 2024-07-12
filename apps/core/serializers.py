from rest_framework import serializers
from .models import Prescription
class PrescriptionSerializer(serializers.Serializer):
    class Meta:
        model = Prescription
        fields = '__all__'