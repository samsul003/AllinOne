from django import forms
from django.forms import ModelForm
from user_manager.models import AllUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class UserRegistrationFrom(ModelForm):

    class Meta:
        model = AllUser
        fields = ['email', 'password', 'name']


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_action = 'login'


    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)



