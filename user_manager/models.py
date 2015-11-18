from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class AllUser(AbstractBaseUser):
    email = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now=True)

    def __unicode__(self):

        return self.email



