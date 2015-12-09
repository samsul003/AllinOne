from django import template
from django.utils import timezone
from datetime import timedelta

from main_app.models import CategoryByUser, Item

register = template.Library()


@register.assignment_tag
def user_categories(user):
    usr_categories = CategoryByUser.objects.filter(user=user)
    return usr_categories


# ### today
@register.simple_tag(takes_context=True)
def this_week_0(context, user):
    today = timezone.now()
    today = today - timedelta(days=0)

    this_day = Item.objects.filter(user=user, purchase_date=today)
    context['this_day'] = this_day
    return ''


# ## 1 day ago
@register.simple_tag(takes_context=True)
def this_week_1(context, user):
    today = timezone.now()
    today = today - timedelta(days=1)
    day_2 = Item.objects.filter(user=user, purchase_date=today)
    context['day_2'] = day_2

    return ''


# ## 2 day ago
@register.simple_tag(takes_context=True)
def this_week_2(context, user):
    today = timezone.now()
    today = today - timedelta(days=2)
    day_3 = Item.objects.filter(user=user, purchase_date=today)
    context['day_3'] = day_3
    return ''


@register.simple_tag(takes_context=True)
def this_week_3(context, user):
    today = timezone.now()
    today = today - timedelta(days=3)
    day_3 = Item.objects.filter(user=user, purchase_date=today)
    context['day_3'] = day_3
    return ''


@register.simple_tag(takes_context=True)
def this_week_4(context, user):
    today = timezone.now()
    today = today - timedelta(days=4)
    day_4 = Item.objects.filter(user=user, purchase_date=today)
    context['day_4'] = day_4
    return ''


@register.simple_tag(takes_context=True)
def this_week_5(context, user):
    today = timezone.now()
    today = today - timedelta(days=5)
    day_5 = Item.objects.filter(user=user, purchase_date=today)
    context['day_5'] = day_5
    return ''


@register.simple_tag(takes_context=True)
def this_week_6(context, user):
    today = timezone.now()
    today = today - timedelta(days=6)
    day_6 = Item.objects.filter(user=user, purchase_date=today)
    context['day_5'] = day_6
    return ''

