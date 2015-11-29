from django import template
from django.core.urlresolvers import reverse


register = template.Library()

# Not used
@register.filter
def is_request_from_register_view(path):
    print path
    if path == reverse('register'):
        return True
    return False
