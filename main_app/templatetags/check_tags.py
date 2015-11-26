from django import template
from django.core.urlresolvers import reverse

register = template.Library()
@register.filter
def is_request_from_register_view(request=None):
    print request
    if request == reverse('register'):
        return True
    return False
