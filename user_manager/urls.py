from django.conf.urls import include, url
from user_manager.views import LoginView, UserRegistrationView, EmailVeriFicationView

urlpatterns = [

    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^register/', UserRegistrationView.as_view(), name='register'),
    url(r'^verify/(?P<token>\w+)/$', EmailVeriFicationView.as_view(), name='verify'),


]