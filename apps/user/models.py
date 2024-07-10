from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from datetime import datetime
#from phonenumber_field.modelfields import PhoneNumberField
import uuid
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = "Male", _('Male')
        FEMALE = "Female", _('Female')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, max_length=50)
    country = CountryField(verbose_name = _("Country"), default="NG", blank=False, null=False)
    phone_number = models.IntegerField(verbose_name = _("Phone Number"), blank=False, null=False)
    medical_history = models.TextField(verbose_name = _("Medical History"), help_text = _("Tell us of any relevant medical report. Allergies, surgeries, chronic illness, etc") )
    dob = models.DateField(verbose_name=_("Date of birth"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    is_patient = models.BooleanField(verbose_name=_("A Patient"), default=True, blank=False, null=False)
    is_staff =  models.BooleanField(verbose_name=_("A Staff"), default=False, blank=False, null=False)
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True, blank=False, null=False)

