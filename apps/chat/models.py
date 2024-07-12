from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.

class Message(models.Model):
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)