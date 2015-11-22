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


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)



