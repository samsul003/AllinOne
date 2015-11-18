from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView
from user_manager.forms import LoginForm, UserRegistrationFrom


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class UserRegistrationView(FormView):
    form_class = UserRegistrationFrom
    template_name = 'registration.html'
    success_url = reverse_lazy('home')




