# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from email_app.models import VerificationCode
from user_manager.forms import LoginForm
from user_manager.models import AllUser


class EmailVeriFicationView(View):
    def dispatch(self, request, *args, **kwargs):

        """
        :param request:
        :param args:
        :param kwargs:
        :return:

        remove the record containing token and email id field after ensuring that this token was assigned
        to this email. If the token is not in the db then the user is trying to make request with bogus token.

        """
        message = ""
        if request.method=="GET":
            token = kwargs['token']
            try:
                ver_code_obj = VerificationCode.objects.get(token=token)
                user = AllUser.objects.get(email=ver_code_obj.email)
                if user.email_verified:
                    message = " You are already verified user."
                else:
                    # delete record fro table. and mark the email as verified.
                    ver_code_obj.delete()
                    user.email_verified = True
                    user.save()
                    message = " You have successfully verified your email"
            except:
                message = " Exception occured. Something went wrong ! " \
                          "Click Request button to get new verification email."


        return render(request,'error.html', {'error':message, 'login_form':LoginForm()})



