from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView, CreateView, TemplateView, RedirectView, View
from AllInOne.settings import EMAIL_HOST_USER
from email_app.models import VerificationCode
import uuid
from user_manager.forms import LoginForm, UserRegistrationFrom
from user_manager.models import AllUser



class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class UserRegistrationView(CreateView):
    form_class = UserRegistrationFrom
    template_name = 'registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):


        recipient = form.cleaned_data['email']
        unique_code = uuid.uuid4().get_hex()
        token_obj = VerificationCode(token=unique_code, email=recipient)
        token_obj.save()
        message = "Please click the link http://127.0.0.1:8000/user/verify/{0}/".format(unique_code)
        print message

        email = EmailMessage('Subject', message, EMAIL_HOST_USER, [recipient, 'sajidur.rahman@particulate.me'])
        email.send()
        return super(UserRegistrationView, self).form_valid(form)


class EmailVeriFicationView(View):
    def dispatch(self, request, *args, **kwargs):
        message = ""
        if(request.method=="GET"):
            token = kwargs['token']
            ver_code_obj = VerificationCode.objects.get(token=token)
            user = AllUser.objects.get(email=ver_code_obj.email)
            if user.email_verified:
                message = " You are already verified user."
        return super(EmailVeriFicationView, self).dispatch(request, *args, **kwargs)