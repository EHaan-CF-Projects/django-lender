from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def get_date(value):
    return value.strftime('%b %d %Y')
