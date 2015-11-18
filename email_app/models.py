from django.db import models

# Create your models here.
from user_manager.models import AllUser


class VerificationCode(models.Model):
    token = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=False, max_length=100)