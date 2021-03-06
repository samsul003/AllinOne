from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import FormView, CreateView, TemplateView, RedirectView, View
from AllInOne.settings import EMAIL_HOST_USER
from email_app.models import VerificationCode
import uuid

from main_app.custom_context_processor import next_param
from user_manager.forms import LoginForm, UserRegistrationFrom
from user_manager.models import AllUser
from django.contrib.auth import login, authenticate, logout
from main_app.models import Item, Category
from user_manager.models import AllUser
from django.utils import timezone
from datetime import date, timedelta, datetime


class UserRegistrationView(CreateView):
    form_class = UserRegistrationFrom
    template_name = 'registration.html'
    success_url = reverse_lazy('error')

    def form_valid(self, form):
        recipient = form.cleaned_data['email']
        unique_code = uuid.uuid4().get_hex()
        token_obj = VerificationCode(token=unique_code, email=recipient)
        token_obj.save()
        message = "Please click the link http://127.0.0.1:8000/user/verify/{0}/".format(unique_code)
        result = self.get_context_data()
        result.update({'error': "Email Sent"})

        email = EmailMessage('Subject', message, EMAIL_HOST_USER, [recipient, 'sajidur.rahman@particulate.me'])
        email.send()
        return super(UserRegistrationView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, 'error.html', {'error': 'You are already a registered user'})
        else:
            return super(UserRegistrationView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        result = super(UserRegistrationView, self).get_context_data(**kwargs)
        result.update({'error': "Email Sent"})
        return result

    def get_success_url(self):
        path = reverse_lazy('error')
        url = "{0}{1}".format(path, "?param=email_sent")

        return url


class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy('dash_board')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        referrer = self.request.POST.get('referrer')
        user = authenticate(email=email, password=password)

        if user is not None:
            # if user.is_active:
            login(self.request, user)
            if referrer !="":
                self.success_url = referrer
            return super(LoginView, self).form_valid(form)
        else:

            return render(self.request, "login.html", {'form': form, 'login_error_message': "Invalid username and password."})

    def get_context_data(self, **kwargs):
        result = super(LoginView, self).get_context_data( **kwargs)
        param = self.request.GET.get('next', '')
        result.update({'param': param})
        return result

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('dash_board')

        if request.user.is_authenticated():
            self.success_url = reverse_lazy('dash_board')
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    if request.method == "GET":
        logout(request)
        return HttpResponseRedirect(reverse_lazy('login'))
    else:
        return HttpResponse(" Crap !")


#@login_required(login_url=reverse_lazy('login'))



