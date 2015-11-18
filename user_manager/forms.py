from django import forms
from django.forms import ModelForm

from user_manager.models import AllUser


class LoginForm(ModelForm):

     class Meta:
        model = AllUser
        fields = ['email', 'password', ]


class UserRegistrationFrom(ModelForm):

    class Meta:
        model = AllUser
        fields = ['email', 'password', 'name']