"""AllInOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main_app import views as main_app_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_app_views.IndexView.as_view(), name='home'),
    url(r'^add/item/', main_app_views.AddItemView.as_view(), name='add_item'),
    url(r'^add/category/', main_app_views.AddCategoryView.as_view(), name='add_category'),
    url(r'^delete/category/$', main_app_views.delete_category, name='cat_delete'),

    # url(r'add/category/', main_app_views.AddCategoryView.as_view(), name='add_category'),
    url(r'^today/', main_app_views.TimeLineView.as_view(), name='time_line'),
    url(r'^categories/', main_app_views.Categories.as_view(), name='categories'),
    url(r'^user/', include('user_manager.urls')),

]
