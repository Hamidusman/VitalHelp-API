from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email


class UserManager(BaseUserManager):   

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email"))
 
    def create_user(
        self,
        email,
        password,
        **extra_fields
    ):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)
