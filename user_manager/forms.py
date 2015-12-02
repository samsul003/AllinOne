from django import forms
from django.forms import ModelForm
from user_manager.models import AllUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, HTML



class UserRegistrationFrom(ModelForm):

    retype_password = forms.CharField(max_length=100, label='Re-enter your password', widget=forms.PasswordInput)

    class Meta:
        model = AllUser
        fields = ['name', 'email', 'password', ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationFrom, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userRegistrationFrom'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))
        self.helper.form_action = 'register'

    def clean(self):

        cleaned_data = super(UserRegistrationFrom, self).clean()
        password = cleaned_data['password']
        password2 = cleaned_data['retype_password']

        if password != password2:
            # msg = " The two passwords you typed do not match. Please try again."
            # self.aad_error('retype_password', msg)
            self.fields['retype_password'].widget.attrs['class'] = 'error'
            self.fields['password'].widget.attrs['class'] = 'error'
            raise forms.ValidationError(" The two passwords you typed do not match. Please try again.")




class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-login_form'
        self.helper.form_class = 'form-inline'
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())



