from django import forms
from django.forms import ModelForm
from user_manager.models import AllUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserRegistrationFrom(ModelForm):

    class Meta:
        model = AllUser
        fields = ['email', 'password', 'name']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationFrom, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userRegistrationFrom'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))
        self.helper.form_action = 'register'


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)



