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


def user_categories(request):
    usr_categories = CategoryByUser.objects.filte(user=request.user)
    return usr_categories


# ### today
def this_week_0(request):
    today = timezone.now()
    today = today - timedelta(days=0)

    this_day = Item.objects.filter(user=request.user, purchase_date=today)
    return this_day


# ## 1 day ago
def this_week_1(request):
    today = timezone.now()
    today = today - timedelta(days=1)

    this_day = Item.objects.filter(user=request.user, purchase_date=today)
    return this_day

# ## 2 day ago
def this_week_0(request):
    today = timezone.now()
    today = today - timedelta(days=1)

    this_day = Item.objects.filter(user=request.user, purchase_date=today)
    return this_day

