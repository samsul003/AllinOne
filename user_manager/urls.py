from django.conf.urls import include, url
from email_app.views import EmailVeriFicationView
from user_manager.views import LoginView, UserRegistrationView, logout_view, DashBoardView

urlpatterns = [

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/', UserRegistrationView.as_view(), name='register'),
    url(r'^verify/(?P<token>\w+)/$', EmailVeriFicationView.as_view(), name='verify'),
    url(r'^dashboard/$', DashBoardView.as_view(),         name='dash_board'),


]