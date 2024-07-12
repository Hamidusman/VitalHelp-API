from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname',
                  'gender', 'user', 'country', 'dob',
                  'medical_history', 'phone_number', 'is_patient',
                  'is_staff'] 
        read_only_fields = ['is_patient', 'is_staff']

        