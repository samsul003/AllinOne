from django import forms
from django.forms import ModelForm
from user_manager.models import AllUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'



