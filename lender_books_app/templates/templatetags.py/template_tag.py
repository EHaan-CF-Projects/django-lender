from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def get_date_string(value):
    value = value[::-1]