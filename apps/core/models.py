from django.db import models
from apps.user.models import Patient, Doctor

# Create your models here.

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=120)
    instruction = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.instruction