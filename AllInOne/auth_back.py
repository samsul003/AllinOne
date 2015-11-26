from django.contrib.auth.models import User
from user_manager.models import AllUser


class MyCustomBackend(object):

    def authenticate(self, email=None, password=None):
         try:
             o = AllUser.objects.get(email=email, password=password)
         except AllUser.DoesNotExist:

                 return None
         return AllUser.objects.get(email=o.email)

    def get_user(self, user_id):
        try:
            return AllUser.objects.get(pk=user_id)
        except AllUser.DoesNotExist:
            return None