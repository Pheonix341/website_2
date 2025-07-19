# products/templatetags/number_filters.py

from django import template

register = template.Library()

@register.filter
def format_thousands(value):
    try:
        return '{0:,}'.format(int(value)).replace(',', ' ')
    except (ValueError, TypeError):
        return value
