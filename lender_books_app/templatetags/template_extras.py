from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def get_date(value):
    """Truncate date to Month Day Year format.
    """
    return value.strftime('%b %d %Y')
