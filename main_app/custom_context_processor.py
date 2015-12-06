from main_app.models import Category, CategoryByUser, Item
from user_manager.forms import LoginForm
from django.utils import timezone
from datetime import date, datetime, timedelta


def categories(request):

    return {'categories': Category.objects.all()}


def next_param(request, next_val=""):
    return {'next_param': next_val}


def login_form(request):
    log_form = LoginForm()
    return log_form


