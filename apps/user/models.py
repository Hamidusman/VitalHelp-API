from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from datetime import datetime
#from phonenumber_field.modelfields import PhoneNumberField
import uuid
class UserManager(BaseUserManager):
    
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email"))

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(
        self,
        email,
        password,
        **extra_fields
    ):
        extra_fields.setdefault("is_doctor", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_doctor") is not True:
            raise ValueError("Superusers must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusers must have is_superuser=True")

        if not password:
            raise ValueError("Superusers must have a password")

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address is required"))

        user = self.create_user(
            email, password, **extra_fields
        )
        user.save(using=self._db)
        return user


class Gender(models.TextChoices):
    MALE = "Male", _('Male')
    FEMALE = "Female", _('Female')
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    objects = UserManager()

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, max_length=50)
    country = CountryField(verbose_name = _("Country"), default="NG", blank=False, null=False)
    phone_number = models.IntegerField(verbose_name = _("Phone Number"), blank=False, null=False)
    dob = models.DateField(verbose_name=_("Date of birth"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    


class Patient(User):
    medical_history = models.TextField(verbose_name = _("Medical History"), help_text = _("Tell us of any relevant medical report. Allergies, surgeries, chronic illness, etc") )
    is_patient = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.firstname + ' ' + self.lastname

    def __str__(self) -> str:
        return self.firstname + ' ' + self.lastname


class Doctor(models.Model):
    specialty = models.TextField(verbose_name = _("specialty"))
    is_staff= models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.firstname + '' + self.lastname
      



    def __str__(self) -> str:
        return self.firstname + '' + self.lastname
      



