from django.conf.urls import include, url
from user_manager.views import LoginView, UserRegistrationView

urlpatterns = [

    url(r'^login/', LoginView.as_view(), name='login'),
     url(r'^register/', UserRegistrationView.as_view(), name='register'),


]