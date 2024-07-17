from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django_countries.fields import CountryField
import uuid
from rest_framework import serializers, generics

class Gender(models.TextChoices):
    MALE = "Male", _('Male')
    FEMALE = "Female", _('Female')

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class AbstractUserProfile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, max_length=6)
    country = CountryField(verbose_name=_("Country"), default="NG")
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=15)
    dob = models.DateField(verbose_name=_("Date of birth"), default='22/22/2222')

    class Meta:
        abstract = True

class Patient(AbstractUserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    medical_history = models.TextField(verbose_name=_("Medical History"), help_text=_("Tell us of any relevant medical report. Allergies, surgeries, chronic illness, etc."))
    is_patient = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Doctor(AbstractUserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.TextField(verbose_name=_("Specialty"))
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
